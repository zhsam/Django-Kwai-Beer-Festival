from django.db import models
from django.db.models.signals import pre_save, post_save

from .utils import unique_slug_generator

class BarsLocation(models.Model):
    name            = models.CharField(max_length=120)
    location        = models.CharField(max_length=120, null=True, blank=True)
    category        = models.CharField(max_length=120, null=True, blank=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    #my_date_field   = models.DateField(auto_now=False, auto_now_add=False)
    slug            = models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.name
    @property
    def title(self):
        return self.name # obj.title

def bl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
# def bl_post_save_receiver(sender, instance, created, *args, **kwargs):
#     print('saved')
#     print(instance.timestamp)
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#         instance.save()
#
pre_save.connect(bl_pre_save_receiver, sender=BarsLocation)
# post_save.connect(bl_post_save_receiver, sender=BarsLocation)
