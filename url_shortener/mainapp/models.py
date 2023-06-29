from django.db import models
from random import choice

def gen_key():
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    key = ''.join([choice(chars) for x in range(6)])
    key = 'ababab'
    return key

class Link(models.Model):
    link = models.CharField(max_length=300)
    key = models.CharField(max_length=200, default=gen_key(), editable=False, unique=True)

    def save(self, *args, **kwargs):
        print(args)
        print(kwargs)
        super().save(*args, **kwargs)  # Call the "real" save() method.


    def __str__(self):
        return self.link
