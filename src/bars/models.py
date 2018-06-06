from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse

from .utils import unique_slug_generator
from .validators import validate_category

User = settings.AUTH_USER_MODEL

class BarsLocation(models.Model):
    owner           = models.ForeignKey(User) # Django Models Unleashed JOINCFE.com
    name            = models.CharField(max_length=120)
    location        = models.CharField(max_length=120, null=True, blank=True)
    category        = models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    #my_date_field   = models.DateField(auto_now=False, auto_now_add=False)
    slug            = models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return f"/bars/{self.slug}"
        return reverse('bars:detail', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.name # obj.title

def bl_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.category = instance.category.capitalize()
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
