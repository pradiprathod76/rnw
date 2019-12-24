from django.shortcuts import render,get_object_or_404
from . import models
from .form import ContecForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    qs_project = models.Project.objects.all()
    qs_service = models.Service.objects.all()
    qs_review = models.Review.objects.all()
    qs_count = models.Count.objects.all()
    contex = {
        'project':qs_project,
        'service':qs_service,
        'review':qs_review,
        'count':qs_count,
        
    }
    return render(request,'index.html',contex)

def about(request):
    qs_about = models.About.objects.all()
    qs_count = models.Count.objects.all()
    qs_team = models.Team.objects.all()
    qs_review = models.Review.objects.all()
    contex = {
        'about':qs_about,
        'rating':qs_count,
        'team':qs_team,
        'review':qs_review,
    }
    return render(request,'about.html',contex)

@login_required
def BlogView(request):
    qs_blog = models.Blog.objects.all()
    post = models.Blog.objects.all().order_by('-date')[:4]

    contex = {
        'blog':qs_blog,
        'post':post

    }
    return render(request,'blog.html',contex)
def contact(request):
    if request.method == "POST":
        my_form = ContecForm(request.POST)
        if my_form.is_valid():
            my_form.save()
    else :
        my_form = ContecForm()

    contex = {
        'form':ContecForm
    }
    return render(request,'contact.html',contex)



def faq(request):
    qs_faq = models.Faq.objects.all()
   
    contex = {
        'faq':qs_faq,
        
    }
    return render(request,'faq.html',contex)

def project_details(request,id):
    project = get_object_or_404(models.Project,id=id)
    contex= {
        'project':project
    }
    return render(request,'project-details.html',contex)
@login_required
def project(request):
    qs_project = models.Project.objects.all()
   
    contex = {
        'project':qs_project,
        
    }
    return render(request,'project.html',contex)


def review(request):
    qs_review = models.Review.objects.all()
   
    contex = {
        'review':qs_review,
        
    }
    return render(request,'review.html',contex)

def service_details(request,id):
    service = get_object_or_404(models.Service,id=id)
    contex= {
        'service':service
    }
    return render(request,'service-details.html',contex)

def service(request):
    qs_service = models.Service.objects.all()
   
    contex = {
        'service':qs_service,
        
    }

    return render(request,'service.html',contex)

def single_blog(request,id):
    blog = get_object_or_404(models.Blog,id=id)
    post = models.Blog.objects.all().order_by('-date')[:4]
    contex= {
        'blog':blog,
        'post':post
    }
    return render(request,'single-blog.html',contex)

def sport(request):
    blog = models.Blog.objects.filter(cat='sport')
    post = models.Blog.objects.all().order_by('-date')[:4]
    contex = {
        'blog':blog,
        'post':post
    }
    return render(request,'cat.html',contex)

def health(request):
    blog = models.Blog.objects.filter(cat='health')
    post = models.Blog.objects.all().order_by('-date')[:4]
    contex = {
        'blog':blog,
        'post':post
    }
    return render(request,'cat.html',contex)

def product(request):
    blog = models.Blog.objects.filter(cat='product')
    post = models.Blog.objects.all().order_by('-date')[:4]
    contex = {
        'blog':blog,
        'post':post
    }
    return render(request,'cat.html',contex)