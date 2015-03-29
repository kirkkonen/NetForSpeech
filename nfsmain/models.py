from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your models here.


class ManagedEntityMixIn():
    # submitted_by = models.ForeignKey()
    submitted_at = models.DateField(auto_now_add=True)


class Organisation(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:organisation_detail', kwargs={'pk': self.pk})


class Media(models.Model):
    name = models.CharField(max_length=512, default='[ИМЯ НЕ ПРИСВОЕНО]')
    home_url = models.CharField(max_length=512, blank=True)
    state = models.CharField(choices=[('Y', 'Да'), ('N', 'Нет')], max_length=1, default='N')

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=512)


class Communication(models.Model):
    pass


class CommunicationMixIn():
    # FIXME Makemigrations throws and error when moving O2OField comm to the mixin

    def save(self, *args, **kwargs):
        if not self.comm_id:
            comm = Communication()
            comm.save()
            self.comm = comm
        return super().save(*args, **kwargs)


class Interview(CommunicationMixIn, models.Model):
    comm = models.OneToOneField(Communication, primary_key=True, blank=True)
    origin = models.ForeignKey(Media)


class Speech(CommunicationMixIn, models.Model):
    comm = models.OneToOneField(Communication, primary_key=True, blank=True)
    origin = models.ForeignKey(Event)


PERSONAL_LINK_TYPES = [
    ('FB', 'Facebook'),
    ('VK', 'Вконтакте'),
    ('TW', 'Twitter'),
    ('GB', 'Личный блог'),
]


class Speaker(models.Model):
    index_name = models.CharField(max_length=256)
    secondary_names = models.CharField(max_length=256)
    other_names = models.CharField(max_length=256, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    current_work = models.ForeignKey(Organisation, blank=True, null=True, related_name='employee_current_set')
    previous_work = models.ManyToManyField(Organisation, blank=True, related_name='employee_former_set')

    def __str__(self):
        return ' '.join([self.index_name, self.secondary_names, self.other_names])

    def get_absolute_url(self):
        return reverse('main:speaker_detail', kwargs={'pk': self.pk})


class PersonalLink(models.Model):
    type = models.CharField(choices=PERSONAL_LINK_TYPES, max_length=2)
    uri = models.CharField(max_length=512)
    speaker = models.ForeignKey(Speaker)


class ThemeTag(models.Model):
    caption = models.CharField(max_length=128)


# TODO Убрать другую сторону related_name для всех наследников Record
class Record(models.Model):
    text = models.TextField()
    datestamp = models.DateField(default=timezone.now)
    timestamp = models.TimeField(blank=True, null=True)
    source_url = models.CharField(max_length=2048)
    media = models.ForeignKey(Media, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # Сначала проверяем, существует ли СМИ, если нужно - создаём
        medias = Media.objects.all()

        for media in medias:
            if media.home_url in self.source_url:
                break
        else:
            media = Media(home_url=self.source_url)
            media.save()

        self.media = media
        super(Record, self).save(*args, **kwargs)

    def related(self):
        return 'Противоречивых фактов: {}, высказываний: {}. ' \
               'Подтверждающих фактов: {}, высказываний: {}'.format(*self.related_count())


class Statement(Record):
    theme_tag = models.CharField(max_length=256, blank=True)
    speaker = models.ForeignKey(Speaker)
    communication = models.CharField(max_length=256, blank=True)
    # communication = models.ForeignKey(Communication)
    statements = models.ManyToManyField('self', blank=True, through='StatementStatementRelation', symmetrical=False)

    def __str__(self):
        return '«{}...» от {}'.format(self.text[:50], self.speaker)

    def get_absolute_url(self):
        return reverse('main:statement_detail', kwargs={'pk': self.pk})

    def related_count(self):
        return [
            self.factstatementrelation_set.filter(relation_type='C').count(),  # факты, противоречащие высказыванию
            self.statements_fst_set.filter(relation_type='C').count(),  # высказывания, противоречащие высказыванию
            self.factstatementrelation_set.filter(relation_type='A').count(),  # факты, подтверждающие высказывание
            self.statements_fst_set.filter(relation_type='A').count(),  # высказывания, подтверждающие высказывание
        ]


class Fact(Record):
    statements = models.ManyToManyField(Statement, blank=True, through='FactStatementRelation')
    facts = models.ManyToManyField('self', blank=True, through='FactFactRelation', symmetrical=False)

    def __str__(self):
        return '«{}...» от {}'.format(self.text[:50], self.media)

    def get_absolute_url(self):
        return reverse('main:fact_detail', kwargs={'pk': self.pk})

    def related_count(self):
        return [
            self.facts_fst_set.filter(relation_type='C').count(),  # факты, противоречащие факту
            self.factstatementrelation_set.filter(relation_type='C').count(),  # высказывания, противоречащие факту
            self.facts_fst_set.filter(relation_type='A').count(),  # факты, подтверждающие факт
            self.factstatementrelation_set.filter(relation_type='A').count(),  # высказывания, подтверждающие факт
        ]


class RecordRelation(models.Model):
    relation_type = models.CharField(choices=[('C', 'Противоречит'), ('A', 'Соответствует')], max_length=1)

    class Meta:
        abstract = True


class SymmetricalRelationMixIn():
    pass


class FactStatementRelation(RecordRelation):
    statement = models.ForeignKey(Statement)
    fact = models.ForeignKey(Fact)

    class Meta:
        unique_together = ('statement', 'fact')


class StatementStatementRelation(RecordRelation):
    statement = models.ForeignKey(Statement, related_name='statements_fst_set')
    statement_2 = models.ForeignKey(Statement, related_name='statements_snd_set')

    def save(self, *args, **kwargs):
        if 'saving_reverse' not in kwargs:
            reverse_relation = StatementStatementRelation(statement=self.statement_2, statement_2=self.statement,
                                                          relation_type=self.relation_type)
            kwargs['saving_reverse'] = True
            reverse_relation.save(*args, **kwargs)
        del kwargs['saving_reverse']
        return super(StatementStatementRelation, self).save(self, *args, **kwargs)

    class Meta:
        unique_together = ('statement', 'statement_2')


class FactFactRelation(RecordRelation):
    fact = models.ForeignKey(Fact, related_name='facts_fst_set')
    fact_2 = models.ForeignKey(Fact, related_name='facts_snd_set')

    def save(self, *args, **kwargs):
        if 'saving_reverse' not in kwargs:
            reverse_relation = FactFactRelation(fact=self.fact_2, fact_2=self.fact, relation_type=self.relation_type)
            kwargs['saving_reverse'] = True
            reverse_relation.save(*args, **kwargs)
        del kwargs['saving_reverse']
        return super(FactFactRelation, self).save(self, *args, **kwargs)

    class Meta:
        unique_together = ('fact', 'fact_2')