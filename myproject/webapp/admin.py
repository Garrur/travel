from django.contrib import admin
from webapp.models import Blog

class _Blog(admin.ModelAdmin):
    list_display=('text',)
# class Signin(admin.ModelAdmin):
#     list_display=('Username','Password','FaviouriteCity','Rating')

admin.site.register(Blog,_Blog)
# admin.site.register(signin,Signin)    
# Register your models here.
