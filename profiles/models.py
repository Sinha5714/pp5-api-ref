from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=True)
    about_me = models.TextField(blank=True)
    instagram_link = models.URLField(max_length=200, blank=True)
    facebook_link = models.URLField(max_length=200, blank=True)
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True)
    profile_pic = models.ImageField(
        upload_to='images/', default='../avatar_zavejy'
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.user}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_profile, sender=User)
