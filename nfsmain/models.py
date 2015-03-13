from django.db import models
from django.core.urlresolvers import reverse
from cities_light.models import City

# Create your models here.


class Organisation(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class Media(models.Model):
    name = models.CharField(max_length=512, default='[ИМЯ НЕ ПРИСВОЕНО]')
    home_url = models.CharField(max_length=512, blank=True)
    state = models.CharField(choices=[('Y', 'Да'), ('N', 'Нет')], max_length=1, default='N')

    def __str__(self):
        return self.name


class Speaker(models.Model):
    index_name = models.CharField(max_length=256)
    secondary_names = models.CharField(max_length=256)
    other_names = models.CharField(max_length=256, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    city = models.ForeignKey(City, blank=True, null=True)
    current_work = models.ForeignKey(Organisation, blank=True, related_name='employee_current_set')
    previous_work = models.ManyToManyField(Organisation, blank=True, related_name='employee_former_set')

    def __str__(self):
        return ' '.join([self.index_name, self.secondary_names, self.other_names])


class ThemeTag(models.Model):
    caption = models.CharField(max_length=128)


class Record(models.Model):
    text = models.TextField()
    source_url = models.CharField(max_length=2048)
    datestamp = models.DateField()
    timestamp = models.TimeField(blank=True, null=True)
    media = models.ForeignKey(Media, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        medias = Media.objects.all()

        for media in medias:
            if media.home_url in self.source_url:
                break
        else:
            media = Media(home_url=self.source_url)
            media.save()

        self.media = media
        super(Record, self).save(*args, **kwargs)


class Fact(Record):
    def __str__(self):
        return '«{}...» от {}'.format(self.text[:50], self.media)

    def get_absolute_url(self):
        return reverse('main:fact_view', kwargs={'pk': self.pk})


class Statement(Record):
    theme_tag = models.ManyToManyField(ThemeTag, blank=True)
    speaker = models.ForeignKey(Speaker)
    happening = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return '«{}...» от {}'.format(self.text[:50], self.speaker)