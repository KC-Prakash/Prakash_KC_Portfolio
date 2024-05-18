from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name


class ContactDetail(models.Model):
    email = models.EmailField()
    email1 = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    phone1 = models.CharField(max_length=20, blank=True, null=True)
    paddress = models.CharField(max_length=255)
    caddress = models.CharField(max_length=255)

    def __str__(self):
        return self.email


class Skill(models.Model):
    title = models.CharField(max_length=100)
    percentage = models.IntegerField()

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    image1 = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    bio = models.TextField(blank=True)
    bio1 = models.TextField(blank=True)
    bio2 = models.TextField(blank=True)
    bio3 = models.TextField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to='portfolio_images/')

    def __str__(self):
        return self.title


class BlogProject(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=20, unique=True, blank=True)
    subtitle = models.CharField(max_length=100, unique=True, blank=True)
    description = RichTextField()
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.CharField(max_length=50, blank=True)
    tags = models.CharField(max_length=200, blank=True)  # A simple approach to tags
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogProject, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

