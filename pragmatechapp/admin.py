from django.contrib import admin
from .models import Applicant, Message
from django.contrib.auth.models import Group, User

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date_applied')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'sender_email', 'message_subject', 'message_content', 'date_sent')

admin.site.site_header = "Pragmatech - Admin Dashboard" 
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Message, MessageAdmin)
