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
        "address": aboutme.address,
        "phone": aboutme.phone,
        "email": aboutme.email,
        "map_embed_link": aboutme.map_embed_link,
    }
    return render(request, "contact.html", context=context)
