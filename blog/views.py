from django.shortcuts import render,redirect
from .models import Post,Tag
from .forms import blog_form
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import Context, Template
from django.core.paginator import Paginator


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    paginator = Paginator(posts,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    tags = Tag.objects.all()
    return render(request,'blog/post_list.html',{'posts':posts,'tags':tags,"page_obj": page_obj})


def full_post(request,id):
    individual_post = Post.objects.filter(published_date__lte=timezone.now()).get(id=id)
    return render(request,'blog/full_post.html',{'individual_post':individual_post})

@login_required
def upload_blog(request):
    if request.method == 'POST':
        form = blog_form(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('post_list')
    else:
        form=blog_form()

    return render(request,'blog/post_upload.html',{'form':form})


def tagged_blog(request,specific_tag):
    specifc_tag_blogs = Post.objects.filter(blog_tag=specific_tag,published_date__lte=timezone.now())
    required_tag = Tag.objects.get(id=specific_tag)
    return render(request,'blog/tagged_post.html',{'specific_tag_blogs':specifc_tag_blogs,'required_tag':required_tag})


#view to upload a blog (can only be accessed by logged-in users)
#login through django-admin, make sure others cant upload blog with someone else's name
#handle images with static files.
#add tags-compsoc,diode,piston. have a foreign key to the tags model, one to many
#order: upload-view, images,tags
#make sure to remove uname and pass from admin.py
#choices for the tags field in blog model
#images in md- {% static 'images/tiger.jpg' %}
#enforce a max limit for height and width of all images(one of them should be adjusted to preserve the aspect ratio)
#many to many tag relationships