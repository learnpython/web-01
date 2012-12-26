from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    User profile.
    """
    user = models.OneToOneField(
        User, related_name='profile', verbose_name='user'
    )

    company = models.CharField(
        'company name', blank=True, default=None, max_length=32, null=True,
        unique=True
    )

    class Meta:
        db_table = 'zo_userprofile'
        verbose_name = 'user profile'
        verbose_name_plural = 'user profiles'


@receiver(signals.post_save, sender=User)
def auto_create_profile(instance, **kwargs):
    """
    Auto-create user profile if it doesn't exist.
    """
    try:
        UserProfile.objects.get(user=instance)
    except UserProfile.DoesNotExist:
        UserProfile.objects.create(user=instance)
