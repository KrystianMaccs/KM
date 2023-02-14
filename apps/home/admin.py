from django.contrib import admin

from apps.home.models import Navbar, Contact, AboutMe

    
@admin.register(Navbar)
class NavbarAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'subject', 'slug', 'message']
    
@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['name', 'resume', 'description']
