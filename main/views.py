from django.shortcuts import render, get_object_or_404

# Create your views here.
from main.models import Blog


def index (request):
    return render(request, 'main/index.html', {
        'posts': Blog.objects.all()[:5]
    })
def view_post(request, slug):
    return render(request, 'main/view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def about (request):
    return render(request, 'main/about.html')

def blog (request):
    return render(request, 'main/blog.html')

def books (request):
    return render(request, 'main/books.html')