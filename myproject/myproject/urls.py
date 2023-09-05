"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    
    # path('signin/',views.Signin),
    path('service/',views.Service,name='services'),
    path('logout/',views.LogoutPage,name='logout'),
    path('signup/',views.SignupPage),
    path('home/',views.HomePage,name='home'),
    path('login/',views.LoginPage,name='login'),
    path('signup/',views.SignupPage,name='signup'),
    path('explore/',views.Explore),
    path('goa/',views.Goa,name='Goa' ),
    path('assam/',views.Assam,name='ASSAM' ),
    path('andman/',views.Andaman,name='ANDAMAN' ),
    path('jaisalmer/',views.Jaisalmer,name='Jaisalmer' ),
    path('chitrakoot/',views.Chitrakoot,name='CHITRAKOOT' ),
    path('kerala/',views.Kerala,name='KERALA' ),
    path('index/',views.index),
   
]