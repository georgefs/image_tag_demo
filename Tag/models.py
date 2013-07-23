from django.db import models

# Create your models here.


class Image(models.Model):
    url = models.URLField(primary_key=True)
    key = models.CharField(blank=True, null=True, max_length=100)

    def __unicode__(self):
        return self.url


class Log(models.Model):
    image = models.ForeignKey(Image)

    status = models.IntegerField(default=1)
    count = models.IntegerField(default=1)
    delta_seconds = models.FloatField()
    result = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return str(self.pk)
