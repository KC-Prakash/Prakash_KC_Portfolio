from django.contrib import admin
from .models import ContactMessage, BlogProject, ContactDetail, Skill, UserProfile, Project


# Register your models here.

admin.site.register(ContactMessage)

admin.site.register(ContactDetail)

admin.site.register(Skill)

admin.site.register(UserProfile)

admin.site.register(Project)

@admin.register(BlogProject)
class BlogProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'updated_at']
    search_fields = ['title', 'subtitle', 'description']
    prepopulated_fields = {'slug': ('title',)}