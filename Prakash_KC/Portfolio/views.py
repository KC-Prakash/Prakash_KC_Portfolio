from django.shortcuts import render, get_object_or_404
from .forms import ContactForm, UserProfileForm, Project, BlogProject 
from django.contrib import messages
from .models import Skill, ContactDetail



# Create your views here.
def home(request):
    return render(request, "includes/base.html")

def index(request):
    return render(request, "index.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Thank you for your message! We will get in touch with you as soon as possible.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def contact_details(request):
    contacts = ContactDetail.objects.all()
    return render(request, 'contact.html', {'contacts': contacts})


def skills(request):
    skills = Skill.objects.all()
    return render(request, 'skills.html', {'skills': skills})

def about_me(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm()
    return render(request, 'about_me.html', {'form': form})

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})

def blog(request):
    blogprojects=BlogProject.objects.all()
    return render(request,'blog.html',{'blogprojects': blogprojects})

def blog_detail(request, pk):
    blog = get_object_or_404(BlogProject, pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})

