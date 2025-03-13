from django.db import models

# Create your models here.
class MyInformation(models.Model):
    first_name = models.CharField(max_length=255,blank=False, null=False)
    last_name = models.CharField(max_length=255,blank=False, null=False)
    bio = models.CharField(max_length=255, blank=False, null=False)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.first_name
    
    

class SocialMedia(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    username = models.CharField(max_length=20,blank=False,null=False)
    url = models.URLField()

    def __str__(self):
        return self.name
    