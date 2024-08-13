from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
import logging 
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator
from.forms import ContactForm



#posts=[
 #       {'id':1,'title':'post 1','content':'content of post 1'},
  #      {'id':2,'title':'post 2','content':'content of post 2'},
   #     {'id':3,'title':'post 3','content':'content of post 3'},
    #    {'id':4,'title':'post 4','content':'content of post 4'},
    #]
def index(request ):
    blog_title="LATEST POST"
    all_posts=Post.objects.all()

    paginator=Paginator(all_posts,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'blog/index.html',{'blog_title':blog_title,'page_obj':page_obj})
def detail(request,slug):
    #post=next((item for item in posts if item['id']==int(num_id)),None)
    try:
        post=Post.objects.get(slug=slug)
        related_post=Post.objects.filter(category=post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post does not exists!!")
    #logger=logging.getLogger("TESTING")
    #logger.debug(f'post variable is {post}')
    return render(request,'blog/detail.html',{'post':post,'related_posts':related_post})
def old_url_redirect(request):
    return redirect(reverse('blog:new_url'))
def new_url_view(request):
    return HttpResponse("this is New url")

def contact_view(request):
    if request.method=='POST':

        form=ContactForm(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        logger=logging.getLogger("TESTING")
        if form.is_valid():
          logger.debug(f"POST Data is ({form.cleaned_data['name']}) ({form.cleaned_data['email']}) ({form.cleaned_data['message']})")
          success_message='Form has been Submitted'
          return render(request,'blog/contact.html',{'form':form,'success_message': success_message})

        else:
            logger.debug('Form Validation error')

        return render(request,'blog/contact.html',{'form':form,'email':email,'message':message})    

    return render(request,'blog/contact.html')
def about_view(request): 
    return render(request,'blog/about.html')
    


    
