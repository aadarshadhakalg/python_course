from django.shortcuts import render
from .models import Blog

# Create your views here.
def blogs(request):
    blogs = Blog.objects.all()
    return render(request, "blog.html", {"blogs": blogs})


def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, "blog_detail.html", {"blog": blog})