from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    aboutme = models.MyInformation.objects.first()
    socials = models.SocialMedia.objects.all()
    context = {
        "name": f'{aboutme.first_name} {aboutme.last_name}',
        "bio": aboutme.bio,
        "social": socials,
        "photo": aboutme.photo.url,
    }
    return render(request,"index.html", context=context)