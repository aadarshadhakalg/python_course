from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        "name": "Aadarsha Dhakal",
        "bio": "Google Me!!",
        "social": {
            "facebook":"aadarshadhakalg",
            "instagram": "aadarshadhakalg",
            "twitter": "aadarshadhakalg",
            "github": "aadarshadhakalg",
        }
    }
    return render(request,"index.html", context=context)