from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class DummyImage(models.Model):
    image = models.ImageField()
    image_name = models.CharField(max_length=50)

    def __str__(self):
        return self.image_name
