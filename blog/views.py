from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts':posts})


def full_post(request,id):
    individual_post = Post.objects.filter(published_date__lte=timezone.now()).get(id=id)
    return render(request,'blog/full_post.html',{'individual_post':individual_post})