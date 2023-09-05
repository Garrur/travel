from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from webapp.models import Blog
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')


def index(request):
    return render(
   request, 'index.html')


def Service(request):
    return render(
        request, 'service.html'
    )

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
         return HttpResponse('Password Mismatched' )
        else:

         my_user=User.objects.create_user(username=uname,email=email,password=pass1)
         my_user.save()
        # return HttpResponse("User has been created Successfully!")
        return redirect('login')
        print(uname,email,pass1,pass2)

    return render(request,'signup.html')
def LoginPage(request):
    if request.method=='POST':
       username=request.POST.get('username')
       pass1=request.POST.get('pass')
       user=authenticate(request,username=username,password=pass1)
       if user is not None:
          login(request,user)
          return redirect('home')
       else:
          return HttpResponse('username or passsword is incorrect')       
       print(username,pass1)
    return render (request,'login.html')

def LogoutPage(request):
   logout(request)
   return redirect('login')

def Explore(request):
    return render(
        request, 'service.html'
    )

def Goa(request):
    # print('qwe') 
    if request.method=="POST":
       blog = request.POST['blog']
       _blog = Blog(username=request.user.username,text=blog,place='Goa')
       _blog.save()
       print(request.user.username)
    mydata = Blog.objects.filter(place='Goa').values()
    context = {'reviews':mydata}
    return render(
        request, 'goa.html',context
    )

def Assam(request):
    if request.method=="POST":
       blog = request.POST['blog']
       _blog = Blog(username=request.user.username,text=blog,place='Assam')
       _blog.save()
    mydata = Blog.objects.filter(place='Assam').values()
    context = {'reviews':mydata}
    return render(
        request, 'assam.html',context
    )

def Andaman(request):
    if request.method=="POST":
       blog = request.POST['blog']
       _blog = Blog(username=request.user.username,text=blog,place='Andaman')
       _blog.save()
    mydata = Blog.objects.filter(place='Andaman').values()
    context = {'reviews':mydata}
    return render(
        request, 'andman.html',context
    )

def Chitrakoot(request):
    if request.method=="POST":
       blog = request.POST['blog']
       _blog = Blog(username=request.user.username,text=blog,place='Chitrakoot')
       _blog.save()
    mydata = Blog.objects.filter(place='Chitrakoot').values()
    context = {'reviews':mydata}
    return render(
        request, 'chitrakoot.html',context
    )

def Jaisalmer(request):
    if request.method=="POST":
       blog = request.POST['blog']
       _blog = Blog(username=request.user.username,text=blog,place='Jaisalmer')
       _blog.save()
    mydata = Blog.objects.filter(place='Jaisalmer').values()
    context = {'reviews':mydata}
    return render(
        request, 'jaisalmer.html',context
    )

def Kerala(request):
    if request.method=="POST":
       blog = request.POST['blog']
       _blog = Blog(username=request.user.username,text=blog,place='Kerela')
       _blog.save()
    mydata = Blog.objects.filter(place='Kerela').values()
    context = {'reviews':mydata}
    return render(
        request, 'kerala.html',context
    )
