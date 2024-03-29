from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView, DetailView

# Create your views here.
from main.models import Blog, Books
from.forms import CommentForm


def index (request):
    posts = Blog.objects.all()
    books = Books.objects.all()
    return render(request, 'main/index.html', {
        'posts': posts,
        'novels': books
    })

def view_post(request, slug):   
    post = Blog.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

    else:
        form = CommentForm()

    return render(request, 'main/view_post.html', {'post': post, 'form': form})


def about (request):
    return render(request, 'main/about.html')

def blog (request):
    return render(request, 'main/blog.html',{
        'posts': Blog.objects.all()[:5]
    })

def books (request):
    return render(request, 'main/books.html',{
        'novels': Books.objects.all()[:5]    
        })

def get_email (request):
    if request.method == 'POST':
        subform = SubForm(request.POST)

        if subform.is_valid():
            return HttpResponseRedirect('/index/')

    else:
        subform = SubForm()

    return render(request, 'main/view_post.html', {'subform': subform})
    return render(request, 'main/index.html', {'subform': subform})
    return render(request, 'main/about.html', {'subform': subform})
    return render(request, 'main/books.html', {'subform': subform})
    return render(request, 'main/blog.html', {'subform': subform})





    
