from django.contrib import admin

from apps.home.models import Contact, AboutMe, Resume



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'subject', 'message']
    
@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['name', 'resume']