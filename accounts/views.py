from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from posts.models import Post
from posts.models import *
from posts.views import *
from django.http import HttpResponseRedirect, HttpResponse
from django.conf.urls import url

# Create your views here.
def signup(request): #I can make the error more specific just add more if and else statements
    if request.method == 'POST':
        if request.POST['password1'] and request.POST['password2'] and request.POST['email'] and request.POST['username'] and request.POST['firstname'] and request.POST['lastname']:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.get(username=request.POST['username'])
                    return render(request, 'accounts/signup.html', {'error': 'User has been taken or your email is taken'})
                except User.DoesNotExist:
                    user = User.objects.create_user(request.POST['username'], request.POST['email'], password=request.POST['password1'], first_name=request.POST['firstname'], last_name=request.POST['lastname'])
                    login(request, user)
                    return render(request, 'accounts/signup.html')
            else:
                return render(request, 'accounts/signup.html', {'error': 'Passwords Dont Match'})
        else:
            return render(request, 'accounts/signup.html', {'error': 'You are missing a field'})
    else:
        return render(request, 'accounts/signup.html')

def loginview(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']
        user = authenticate(username=username, password= password)
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return redirect('home')
            # Redirect to a success page.`
        # Return an 'invalid login' error message.
        else:
            return render(request, 'accounts/login.html', {'error': 'login doesnt work'})
    else:
        return render(request, 'accounts/login.html')

def logoutview(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def profile(request):
    posts = Post.objects.order_by('votes_total')
    return render(request, 'accounts/profile.html', {'posts': posts}) 

def edit(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(pk=user_id)
        user.profile.firstname = request.POST['firstname']
        user.username = request.POST['username']
        user.email= request.POST['email']    
        user.profile.bio = request.POST['bio']
        user.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) #how do you show it succeeded? and hwo do you redirect to profile page?
    else:
        return render(request, 'accounts/edit.html') 
