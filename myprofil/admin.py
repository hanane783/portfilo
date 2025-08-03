from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile, Skill, Experience, Project, ContactMessage

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job_title', 'email')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'type', 'start_date', 'end_date')
    list_filter = ('type',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'project_url')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sent_at')
    readonly_fields = ('sent_at',)