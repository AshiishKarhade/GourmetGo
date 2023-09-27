from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserProfile


# Django signal - UserProfile should automatically get created when User is created (lets say from createsuperuser
# command)
@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        # if new user is created
        UserProfile.objects.create(user=instance)
    else:
        try:
            # if new user is updated
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # create the new user if it does not exist
            UserProfile.objects.create(user=instance)
