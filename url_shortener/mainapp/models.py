from django.db import models


class Link(models.Model):
    link = models.CharField(max_length=300)
    key = models.CharField(max_length=200, editable=True, unique=True)

    def __str__(self):
        return self.link
