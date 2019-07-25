from django.db import models

# Create your models here.
class article(models.Model):
    title = models.CharField(max_length=255)
    types = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        ordering = ['-id']
