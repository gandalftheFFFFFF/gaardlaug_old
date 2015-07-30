from django.db import models

from blog.models import Post
# Create your models here.

UPLOAD_PATH_CHOICES = (('regnskab', 'Regnskab'),
                       ('referat', 'Referat'),
                       ('andet', 'Andet'))

def get_upload_path(instance, filename):
    return '{category}/{filename}'.format(category=instance.category, filename=filename)


class Uploader(models.Model):
    file_name = models.CharField(max_length=100)
    category = models.CharField(max_length=200, choices=UPLOAD_PATH_CHOICES, default='media')
    upload_date = models.DateTimeField()
    doc = models.FileField(upload_to=get_upload_path)
    post = models.ForeignKey(Post, blank=True, null=True)

    def __str__(self):
        return self.file_name

    class Meta:
        ordering = ['-upload_date']

