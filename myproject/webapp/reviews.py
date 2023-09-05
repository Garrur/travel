from models import Blog
from django import template

register = template.Library()

@register.simple_tag
def reviews():
    mydata = Blog.objects.values()
    