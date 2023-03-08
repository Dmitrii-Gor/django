from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=60, null=False)
    price = models.FloatField(null=False)
    image = models.URLField(max_length=400)
    release_date = models.DateField(null=False)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return self.name
