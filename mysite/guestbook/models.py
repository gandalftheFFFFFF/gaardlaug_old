from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted']