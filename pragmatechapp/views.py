from django.shortcuts import render
from .models import Applicant, Message
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def index(request): 
    context = {
        'applicants': Applicant.objects.all()
    }
    if request.method == "POST":
        applicant_name = request.POST.get('name')
        applicant_email = request.POST.get('email')
        subject = 'Müraciətiniz qəbul olundu'
        message = 'Salam, dəyərli ' + str(applicant_name) + '. \nTezliklə sizinlə əlaqə saxlanılacaq.'
        from_email = settings.SERVER_EMAIL
        recipient_list = [applicant_email]
        send_mail(subject, message, from_email, recipient_list)
        messages.info(request, 'Müraciətiniz qəbul olundu.')
        if request.POST.get('email'):
            Applicant.objects.create(
                name = request.POST.get('name'),
                email = request.POST.get('email'),
                phone = request.POST.get('phone')
            )
    return render(request, 'pragmatechapp/index.html', context)

def about_us(request): 
    return render(request, 'pragmatechapp/about-us.html', {})

def advantages(request):
    return render(request, 'pragmatechapp/pragmatech-ustunlukler.html', {})

def packages(request):
    return render(request, 'pragmatechapp/tedris-paketleri.html', {})

def conditions(request):
    return render(request, 'pragmatechapp/pragmatech-qebul-prosesi.html', {})

def html_css(request):
    return render(request, 'pragmatechapp/html-css.html', {})

def javascript(request):
    return render(request, 'pragmatechapp/javascript.html', {})

def csharp(request):
    return render(request, 'pragmatechapp/csharp.html', {})

def php(request):
    return render(request, 'pragmatechapp/php.html', {})

def python(request):
    return render(request, 'pragmatechapp/python.html', {})

def devsecops(request):
    return render(request, 'pragmatechapp/devsecops.html', {})

def cybersecurity(request):
    return render(request, 'pragmatechapp/cybersecurity.html', {})

def foundation(request):
    return render(request, 'pragmatechapp/foundation.html', {})

def frontend(request):
    return render(request, 'pragmatechapp/frontend-development.html', {})

def backend(request):
    return render(request, 'pragmatechapp/backend-development.html', {})

def contact(request):
    context = {
        'messages': Message.objects.all()
    }
    if request.method == "POST":
        sender_name = request.POST.get('sender_name')
        sender_email = request.POST.get('sender_email')
        message_subject = request.POST.get('message_subject')
        message_content = request.POST.get('message_content')
        subject = 'Mesajınız qəbul olundu'
        message = 'Salam, dəyərli ' + str(sender_name) + '. \nTezliklə sizinlə əlaqə saxlanılacaq.'
        from_email = settings.SERVER_EMAIL
        recipient_list = [sender_email]
        send_mail(subject, message, from_email, recipient_list)
        if request.POST.get('message_content'):
            Message.objects.create(
                sender_name = request.POST.get('sender_name'),
                sender_email = request.POST.get('sender_email'),
                message_subject = request.POST.get('message_subject'),
                message_content = request.POST.get('message_content')
            )
    return render(request, 'pragmatechapp/contact.html', context)

# def coming_soon(request):
#     return render(request, 'pragmatechapp/coming-soon.html', {})