from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import MemberProfile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        MemberProfile.objects.create(user=instance)

@receiver(post_save, sender=MemberProfile)
def update_user(sender, instance, created, **kwargs):
    if not created:
        instance.user.save()
