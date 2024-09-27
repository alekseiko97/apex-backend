from django.db import models
from django.contrib.auth.models import User
# Signal to create a UserProfile when a User is created
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'organization' 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_profile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')

    class Meta:
        db_table = 'category' 
        indexes = [models.Index(fields=['name'])]  # Indexing for better performance

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="No description available")
    categories = models.ManyToManyField(Category, related_name='products')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'product' 
        indexes = [models.Index(fields=['name'])]  # Indexing for better performance