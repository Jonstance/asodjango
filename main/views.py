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
        'books': books
    })

def view_post(request, slug):   
    post = Blog.objects.get(slug=slug)

    if request.method == 'Post':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('view_post', slug=post.slug)
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
        'books': Books.objects.all()
    })