from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .forms import PostForm
from django.core.files.storage import FileSystemStorage
from django.conf.urls import url
from posts.models import *


# Create your views here.
@login_required
def create(request):
    if request.method =='POST':
        if request.POST['title'] and request.POST['body'] and request.POST['image'] and request.FILES['resume']:
            post= Post()
            post.title = request.POST['title']
            post.image = request.FILES['image']
            post.resume = request.FILES['resume']
            post.bodt = request.POST['body']
            post.pub_date =timezone.datetime.now()
            post.author = request.user
            post.save()
            return redirect('home')
        else:
            return render(request, 'posts/create.html', {'error': 'ERROR YOU NEED TO INPUT ALL FIELDS'})
    else:
        return render(request, 'posts/create.html')

def home(request):
    posts = Post.objects.order_by('votes_total')
    return render(request, 'posts/home.html', {'posts': posts})

def upvote(request, pk):
    if request.method =='POST':
        post = Post.objects.get(pk=pk)
        post.votes_total += 1
        post.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def downvote(request, pk):
    if request.method =='POST':
        post = Post.objects.get(pk=pk)
        post.votes_total -= 1
        post.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def blog(request, post_id):
    posts = Post.objects.get(pk=post_id) #so this is getting all the objects of that post_id and calling it post and then u can access inidivual stuff using post.
    allposts = Post.objects.order_by('votes_total')
    return render(request, 'posts/blog.html', {'posts': posts, 'allposts': allposts})

 #dicitonary name for that specific post you now have
                                                                #and the blog.html is where you will redirect everything...
def userposts(request, user_id):
    posts = Post.objects.filter(author__id=user_id)
    author = User.objects.get(pk=user_id)
    return render(request, 'posts/userposts.html', {'author': author, 'posts': posts}) 


def editposts(request, post_id):
    posts = Post.objects.get(pk=post_id)
    if request.method == 'POST':    
        posts.title = request.POST['title']
        posts.body = request.POST['body']
        posts.resume = request.POST['resume']
        posts.image = request.POST['image']
        posts.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) #how do you show it succeeded? and hwo do you redirect to profile page?
    else:
        return render(request, 'posts/editposts.html', {'posts': posts}) 


