from django.shortcuts import render

from .models import MyInformation, SocialMedia
from .forms import ContactMessageForm


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

    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            context["success"] = True
        else:   
            context["form"] = form
    else:
        context["form"] = ContactMessageForm()
    return render(request, "contact.html", context=context)