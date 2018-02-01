from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User,on_delete=None)
    votes_total = models.IntegerField(default=1)
    resume = models.FileField(blank=True, null=True, upload_to='resumes/')
    image = models.ImageField(upload_to='images/', default = 'naruto.png', max_length=100)
    
    def __str__(self):  # __unicode__ for Python 2
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    bio = models.TextField()

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()