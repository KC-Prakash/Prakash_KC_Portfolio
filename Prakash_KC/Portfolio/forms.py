from django import forms
from .models import ContactMessage, Skill ,UserProfile, Project, BlogProject



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['title', 'percentage']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name','image', 'bio', 'facebook', 'instagram']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'subtitle', 'description', 'image']

class BlogProjectForm(forms.ModelForm):
    class Meta:
        model = BlogProject
        fields = ['title', 'subtitle', 'description', 'image', 'status', 'category', 'tags', 'author']