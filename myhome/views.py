# from imaplib import _Authenticator
# from django.shortcuts import render
# from.models import Post
# from.models import Galery
# from.models import Comment
# from.forms import InputForm
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from.models import Post
from.models import Galery
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Comment 

# Create your views here.
def Home(request):
    Posts = Post.objects.all()
    Galerys = Galery.objects.all()
    return(
        render(request,"home.html",{"posts":Posts, "galerys":Galerys}))

def Detail(request, slug):
    post = Post.objects.get(slug=slug)
    Galerys = Galery.objects.all()
    comments = Comment.objects.filter(post=post)
    return(
        render(request,"information.html",{"post":post, "galerys":Galerys ,"comments":comments }))


def Search(request):
    if request.method == "POST":
        result=request.POST['result']
        posts=Post.objects.filter(title__contains = result)
        return render(request,"search.html",{"posts":posts,'result':result })
    else:
        return render(request,'search.html',{})
    
def Addcomment(request):
    if request.method == "POST":
        username = request.POST['username']
        postid = request.POST['postid']
        body = request.POST['body']
        post = Post.objects.get(id = postid)
        slug = request.POST['slug']
        Comment.objects.create(username = username, post = post, body = body )

    return Detail(request=request,slug=slug)

def Signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # username=form.cleaned_data['username']
            # password=form.cleaned_data['password']
            # user=authenticate(username=username,password=password)
    else:
        form = UserCreationForm()

    return (render(request,"signup.html" , {'form':form} ))
# def Signin(request):
#     form = AuthenticationForm()

#     return (render(request,"signin.html",{'form':form}))
def Signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else: 
            messages.warning(request, ("There Was An Error Logging In, Try Again..."))
            return redirect("signin")
    return (
       render(request,"signin.html"))



def Logout(request):
    logout(request)
    messages.success(request, ("You Were Logged Out!"))
    return redirect("home")