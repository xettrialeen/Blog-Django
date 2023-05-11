from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import *
# Create your views here.


# creating home
def home_page(request):
    context = {}
    if request.method == 'GET':
        queryset = BlogPost.objects.latest('pub_date')
        context = {'queryset': queryset}

    return render(request, 'home/index.html', context)


def all_blogs(request):
    context = {}
    if request.method == 'GET':
        queryset = BlogPost.objects.all().order_by('-pub_date')
        context = {'queryset': queryset}

        print("printed")
    return render(request, 'home/blogs.html', context)


def blog_post(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'home/blogpost.html', {'blog_post': blog_post})


# about page

def about_page(request):
    context = {}
    if request.method == 'GET':
        about = AboutPage.objects.first()
        context = {'about': about}
    return render(request, 'about/about.html', context)


def my_view(request):
    my_data = {'title': 'My Page Title', 'content': 'My page content.'}
    return render(request, 'my_template.html', {'my_data': my_data})


def contact_page(request):
    print(request.method)
    if request.method == 'POST':
        print(request.method)
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        message = request.POST.get('Message')

        ContactForm.objects.create(
            name=name,
            email=email,
            message=message
        )


        print(name,email,message)

    return render(request, 'about/contact.html')
