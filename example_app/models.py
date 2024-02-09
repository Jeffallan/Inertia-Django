from django.db import models

class Albums(models.Model):
    artist = models.CharField(max_length=500)
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title
