from django.contrib import admin
from .models import Applicant
from django.contrib.auth.models import Group, User

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')


admin.site.site_header = "Pragmatech - Admin Dashboard" 
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Applicant, ApplicantAdmin)
