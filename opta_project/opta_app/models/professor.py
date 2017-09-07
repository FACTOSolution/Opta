from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Professor(models.Model):
    # Extends User Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Extra fields
    area = models.CharField(max_length=40, blank=True)
    subarea = models.CharField(max_length=40, blank=True)
    lattes = models.URLField(max_length=80, blank=True)

    # Define signals so our Professor model will be automatically
    # created/updated when we create/update User instances
    @receiver(post_save, sender=User)
    def create_user_professor(sender, instance, created, **kwargs):
        if created:
            Professor.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_professor(sender, instance, **kwargs):
        instance.professor.save()
