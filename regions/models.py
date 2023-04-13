from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=125)
    tag = models.CharField(max_length=4, default='')
    parent_region = models.ForeignKey('self',
                                      blank=True,
                                      null=True,
                                      related_name='child_regions',
                                      on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
