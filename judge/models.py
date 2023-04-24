from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from regions.models import Region


class Club(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Judge(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=254, blank=True, default='')
    postcode = models.CharField(max_length=12, blank=True, default='')
    city = models.CharField(max_length=254, blank=True, default='')
    birthday = models.DateField(auto_now=False, auto_now_add=False, null=True)
    phone = models.CharField(max_length=50, blank=True, default='')
    club = models.ForeignKey(
        Club, on_delete=models.PROTECT, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, default=1)
    managed_regions = models.ManyToManyField(
        Region, related_name="managers", blank=True)

    def __str__(self):
        return self.user.get_full_name()


@receiver(post_save, sender=User)
def create_user_judge(sender, instance, created, **kwargs):
    if created:
        Judge.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_judge(sender, instance, **kwargs):
    instance.judge.save()
