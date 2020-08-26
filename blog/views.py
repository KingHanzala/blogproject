from django.shortcuts import render , get_object_or_404
from .models import Blog
# Create your views here.
def allblogs(request):
    blog=Blog.objects
    return render(request,'allblogs.html',{'blog':blog})
def detail(request,blog_id):
    dblog=get_object_or_404(Blog,pk=blog_id)
    return render(request,'details.html',{'blog':dblog})