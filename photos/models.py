from django.conf import settings
from django.db import models

# Create your models here.

def upload_image(instance, filename):
    return "images/{user}/{filename}".format(user=instance.user, filename=filename)


class PhotoQuerySet(models.QuerySet):
    pass

class PhotoManager(models.Manager):
    def get_queryset(self):
        return PhotoQuerySet(self.model, using=self._db)

class Photo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    caption = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_image, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    publish_time = models.DateTimeField(auto_now_add=True)

    objects = PhotoManager()

    def __str__(self):
        return str(self.caption)

    @property
    def owner(self):
        return self.user