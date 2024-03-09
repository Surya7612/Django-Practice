from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': 'Surya',
        'title' : 'Blog 1',
        'content': 'First Blog content',
        'date_posted': 'February 06, 2024'
    },
     {
        'author': 'Shuchi',
        'title' : 'Blog 2',
        'content': 'Second Blog content',
        'date_posted': 'February 07, 2024'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html', {'title': 'About'})
