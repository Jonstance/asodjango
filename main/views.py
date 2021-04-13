from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.
from main.models import Blog


def index (request):
    return render(request, 'main/index.html', {
        'posts': Blog.objects.all()[:5]
    })

class ViewPost(generic.DetailView):
    model = Blog
    template_name = 'main/view_post.html'

def about (request):
    return render(request, 'main/about.html')

def blog (request):
    return render(request, 'main/blog.html')

def books (request):
    return render(request, 'main/books.html')