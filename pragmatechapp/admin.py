from django.contrib import admin
from .models import Applicant, UserMessage
from django.contrib.auth.models import Group, User

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'sender_email', 'message_subject', 'message_content')

admin.site.site_header = "Pragmatech - Admin Dashboard" 
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(UserMessage, UserMessageAdmin)
