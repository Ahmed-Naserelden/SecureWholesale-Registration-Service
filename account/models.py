from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Organizations(models.Model):
    # Add your additional fields here
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    org_id = models.CharField(max_length=255)
    license_id = models.CharField(max_length=255)
    org_status = models.BooleanField()

    org_type = models.CharField(max_length=255)
    license_name = models.CharField(max_length=255)
    org_fin_id = models.CharField(max_length=255)

    finan_limit_from = models.CharField(max_length=255)
    finan_limit_to = models.CharField(max_length=255)
    bank_account = models.CharField(max_length=255)
    
    org_attch = models.CharField(max_length=11)


class Customers(models.Model):
    # Add your additional fields here
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    org_id = models.CharField(max_length=255)
    org_name = models.CharField(max_length=255)
    org_admin_id = models.CharField(max_length=255)

    permission_id = models.CharField(max_length=255)
    user_status = models.BooleanField()


    bus_user_id = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    user_attch = models.CharField(max_length=11)


# sothat when usercreated create token automatic.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def TokenCreate(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
