from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    posted = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-posted']

class Image(models.Model):
    image = models.ImageField(upload_to='')
    post = models.ForeignKey(Post)