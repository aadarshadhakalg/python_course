from django.shortcuts import render

from .models import MyInformation, SocialMedia


def index(request):
    aboutme = MyInformation.objects.first()
    socials = SocialMedia.objects.filter(person=aboutme)
    context = {
        "name": f'{aboutme.first_name} {aboutme.last_name}',
        "bio": aboutme.bio,
        "social": socials,
        "photo": aboutme.photo.url,
    }
    return render(request, "index.html", context=context)


def contact(request):
    aboutme = MyInformation.objects.first()
    context = {
        "email": aboutme.email,
        "phone": aboutme.phone,
        "address": aboutme.address,
        "map_url": aboutme.map_url,
    }
    return render(request, "contact.html", context=context)