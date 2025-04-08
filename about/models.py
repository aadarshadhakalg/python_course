from django.db import models

# Create your models here.


class MyInformation(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    bio = models.CharField(max_length=255, blank=False, null=False)
    photo = models.ImageField(upload_to='photos/')
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    map_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name}'


class SocialMedia(models.Model):
    person = models.ForeignKey(MyInformation, on_delete=models.CASCADE, related_name='social_medias')
    name = models.CharField(max_length=255, blank=False, null=False)
    username = models.CharField(max_length=20, blank=False, null=False)
    url = models.URLField()

    def __str__(self):
        return f'{self.name}'
