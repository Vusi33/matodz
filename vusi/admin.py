from django.contrib import admin
from .models import Contact

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    search_fields = ('name', 'email', 'subject', 'message')

admin.site.register(Contact, ContactMessageAdmin)

