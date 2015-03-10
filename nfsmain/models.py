from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Media(models.Model):
    name = models.CharField(max_length=512, default='[ИМЯ НЕ ПРИСВОЕНО]')
    home_url = models.CharField(max_length=512, blank=True)
    state = models.CharField(choices=[('Y', 'Да'), ('N', 'Нет')], max_length=1, default='N')

    def __str__(self):
        return self.name


class Fact(models.Model):
    text = models.TextField()
    source_url = models.CharField(max_length=2048)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    media = models.ForeignKey(Media, blank=True)

    def __str__(self):
        return '«{}...» от {}'.format(self.text[:50], self.media)

    def get_absolute_url(self):
        return reverse('main:fact_view', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        medias = Media.objects.all()

        for media in medias:
            if media.home_url in self.source_url:
                break
        else:
            media = Media(home_url=self.source_url)
            media.save()

        self.media = media
        super(Fact, self).save(*args, **kwargs)