from django.shortcuts import render
from .models import Applicant, Message
from django.core.mail import send_mail
from django.conf import settings

def index(request): 
    context = {
        'applicants': Applicant.objects.all()
    }
    if request.method == "POST":
        applicant_name = request.POST.get('name')
        applicant_email = request.POST.get('email')
        applicant_phone = request.POST.get('phone')
        subject = 'Müraciətiniz qəbul olundu'
        message = 'Salam, dəyərli ' + str(applicant_name) + '. \nTezliklə sizinlə əlaqə saxlanılacaq.'
        from_email = settings.SERVER_EMAIL
        recipient_list = [applicant_email]
        send_mail(subject, message, from_email, recipient_list)
        if request.POST.get('email'):
            Applicant.objects.create(
                name = request.POST.get('name'),
                email = request.POST.get('email'),
                phone = request.POST.get('phone')
            )
    return render(request, 'pragmatechapp/index.html', context)

def about_us(request): 
    context = {
        'applicants': Applicant.objects.all()
    }
    if request.method == "POST":
        applicant_name = request.POST.get('name')
        applicant_email = request.POST.get('email')
        applicant_phone = request.POST.get('phone')
        subject = 'Müraciətiniz qəbul olundu'
        message = 'Salam, dəyərli ' + str(applicant_name) + '. \nTezliklə sizinlə əlaqə saxlanılacaq.'
        from_email = settings.SERVER_EMAIL
        recipient_list = [applicant_email]
        send_mail(subject, message, from_email, recipient_list)
        if request.POST.get('email'):
            Applicant.objects.create(
                name = request.POST.get('name'),
                email = request.POST.get('email'),
                phone = request.POST.get('phone')
            )
    return render(request, 'pragmatechapp/about-us.html', context)

def advantages(request):
    context = {
        'applicants': Applicant.objects.all()
    }
    if request.method == "POST":
        applicant_name = request.POST.get('name')
        applicant_email = request.POST.get('email')
        applicant_phone = request.POST.get('phone')
        subject = 'Müraciətiniz qəbul olundu'
        message = 'Salam, dəyərli ' + str(applicant_name) + '. \nTezliklə sizinlə əlaqə saxlanılacaq.'
        from_email = settings.SERVER_EMAIL
        recipient_list = [applicant_email]
        send_mail(subject, message, from_email, recipient_list)
        if request.POST.get('email'):
            Applicant.objects.create(
                name = request.POST.get('name'),
                email = request.POST.get('email'),
                phone = request.POST.get('phone')
            )
    return render(request, 'pragmatechapp/pragmatech-ustunlukler.html', context)

def packages(request):
    context = {
        'applicants': Applicant.objects.all()
    }
    if request.method == "POST":
        applicant_name = request.POST.get('name')
        applicant_email = request.POST.get('email')
        applicant_phone = request.POST.get('phone')
        subject = 'Müraciətiniz qəbul olundu'
        message = 'Salam, dəyərli ' + str(applicant_name) + '. \nTezliklə sizinlə əlaqə saxlanılacaq.'
        from_email = settings.SERVER_EMAIL
        recipient_list = [applicant_email]
        send_mail(subject, message, from_email, recipient_list)
        if request.POST.get('email'):
            Applicant.objects.create(
                name = request.POST.get('name'),
                email = request.POST.get('email'),
                phone = request.POST.get('phone')
            )
    return render(request, 'pragmatechapp/tedris-paketleri.html', context)

def conditions(request):
    context = {
        'applicants': Applicant.objects.all()
    }
    if request.method == "POST":
        applicant_name = request.POST.get('name')
        applicant_email = request.POST.get('email')
        applicant_phone = request.POST.get('phone')
        subject = 'Müraciətiniz qəbul olundu'
        message = 'Salam, dəyərli ' + str(applicant_name) + '. \nTezliklə sizinlə əlaqə saxlanılacaq.'
        from_email = settings.SERVER_EMAIL
        recipient_list = [applicant_email]
        send_mail(subject, message, from_email, recipient_list)
        if request.POST.get('email'):
            Applicant.objects.create(
                name = request.POST.get('name'),
                email = request.POST.get('email'),
                phone = request.POST.get('phone')
            )
    return render(request, 'pragmatechapp/pragmatech-qebul-prosesi.html', context)

def html_css(request):
    context = {
        'applicants': Applicant.objects.all()
    }
    if request.method == "POST":
        applicant_name = request.POST.get('name')
        applicant_email = request.POST.get('email')
        applicant_phone = request.POST.get('phone')
        subject = 'Müraciətiniz qəbul olundu'
        message = 'Salam, dəyərli ' + str(applicant_name) + '. \nTezliklə sizinlə əlaqə saxlanılacaq.'
        from_email = settings.SERVER_EMAIL
        recipient_list = [applicant_email]
        send_mail(subject, message, from_email, recipient_list)
        if request.POST.get('email'):
            Applicant.objects.create(
                name = request.POST.get('name'),
                email = request.POST.get('email'),
    return render(request, 'pragmatechapp/html-css.html', context)

def javascript(request):
    context = {
        'applicants': Applicant.objects.all()
    }
    if request.method == "POST":
        applicant_name = request.POST.get('name')
        applicant_email = request.POST.get('email')
        applicant_phone = request.POST.get('phone')
        subject = 'Müraciətiniz qəbul olundu'
        message = 'Salam, dəyərli ' + str(applicant_name) + '. \nTezliklə sizinlə əlaqə saxlanılacaq.'
        from_email = settings.SERVER_EMAIL
        recipient_list = [applicant_email]
        send_mail(subject, message, from_email, recipient_list)
        if request.POST.get('email'):
            Applicant.objects.create(
                name = request.POST.get('name'),
                email = request.POST.get('email'),
    return render(request, 'pragmatechapp/javascript.html', context)

def csharp(request):
    context = {
        'applicants': Applicant.objects.all()
    }
    if request.method == "POST":
        applicant_name = request.POST.get('name')
        applicant_email = request.POST.get('email')
        applicant_phone = request.POST.get('phone')
        subject = 'Müraciətiniz qəbul olundu'
        message = 'Salam, dəyərli ' + str(applicant_name) + '. \nTezliklə sizinlə əlaqə saxlanılacaq.'
        from_email = settings.SERVER_EMAIL
        recipient_list = [applicant_email]
        send_mail(subject, message, from_email, recipient_list)
        if request.POST.get('email'):
            Applicant.objects.create(
                name = request.POST.get('name'),
                email = request.POST.get('email'),
    return render(request, 'pragmatechapp/csharp.html', context)

def php(request):
    context = {
        'applicants': Applicant.objects.all()
    }
    if request.method == "POST":
        applicant_name = request.POST.get('name')
        applicant_email = request.POST.get('email')
        applicant_phone = request.POST.get('phone')
        subject = 'Müraciətiniz qəbul olundu'
        message = 'Salam, dəyərli ' + str(applicant_name) + '. \nTezliklə sizinlə əlaqə saxlanılacaq.'
        from_email = settings.SERVER_EMAIL
        recipient_list = [applicant_email]
        send_mail(subject, message, from_email, recipient_list)
        if request.POST.get('email'):
            Applicant.objects.create(
                name = request.POST.get('name'),
                email = request.POST.get('email'),
    return render(request, 'pragmatechapp/php.html', context)

def python(request):
    context = {
        'applicants': Applicant.objects.all()
    }
    if request.method == "POST":
        applicant_name = request.POST.get('name')
        applicant_email = request.POST.get('email')
        applicant_phone = request.POST.get('phone')
        subject = 'Müraciətiniz qəbul olundu'
        message = 'Salam, dəyərli ' + str(applicant_name) + '. \nTezliklə sizinlə əlaqə saxlanılacaq.'
        from_email = settings.SERVER_EMAIL
        recipient_list = [applicant_email]
        send_mail(subject, message, from_email, recipient_list)
        if request.POST.get('email'):
            Applicant.objects.create(
                name = request.POST.get('name'),
                email = request.POST.get('email'),
    return render(request, 'pragmatechapp/python.html', context)

def devsecops(request):
    context = {
        'applicants': Applicant.objects.all()
    }
    if request.method == "POST":
        applicant_name = request.POST.get('name')
        applicant_email = request.POST.get('email')
        applicant_phone = request.POST.get('phone')
        subject = 'Müraciətiniz qəbul olundu'
        message = 'Salam, dəyərli ' + str(applicant_name) + '. \nTezliklə sizinlə əlaqə saxlanılacaq.'
        from_email = settings.SERVER_EMAIL
        recipient_list = [applicant_email]
        send_mail(subject, message, from_email, recipient_list)
        if request.POST.get('email'):
            Applicant.objects.create(
                name = request.POST.get('name'),
                email = request.POST.get('email'),
    return render(request, 'pragmatechapp/devsecops.html', context)

def cybersecurity(request):
    context = {
        'applicants': Applicant.objects.all()
    }
    if request.method == "POST":
        applicant_name = request.POST.get('name')
        applicant_email = request.POST.get('email')
        applicant_phone = request.POST.get('phone')
        subject = 'Müraciətiniz qəbul olundu'
        message = 'Salam, dəyərli ' + str(applicant_name) + '. \nTezliklə sizinlə əlaqə saxlanılacaq.'
        from_email = settings.SERVER_EMAIL
        recipient_list = [applicant_email]
        send_mail(subject, message, from_email, recipient_list)
        if request.POST.get('email'):
            Applicant.objects.create(
                name = request.POST.get('name'),
                email = request.POST.get('email'),
    return render(request, 'pragmatechapp/cybersecurity.html', context)

def foundation(request):
    context = {
        'applicants': Applicant.objects.all()
    }
    if request.method == "POST":
        applicant_name = request.POST.get('name')
        applicant_email = request.POST.get('email')
        applicant_phone = request.POST.get('phone')
        subject = 'Müraciətiniz qəbul olundu'
        message = 'Salam, dəyərli ' + str(applicant_name) + '. \nTezliklə sizinlə əlaqə saxlanılacaq.'
        from_email = settings.SERVER_EMAIL
        recipient_list = [applicant_email]
        send_mail(subject, message, from_email, recipient_list)
        if request.POST.get('email'):
            Applicant.objects.create(
                name = request.POST.get('name'),
                email = request.POST.get('email'),
    return render(request, 'pragmatechapp/foundation.html', context)

def frontend(request):
    context = {
        'applicants': Applicant.objects.all()
    }
    if request.method == "POST":
        applicant_name = request.POST.get('name')
        applicant_email = request.POST.get('email')
        applicant_phone = request.POST.get('phone')
        subject = 'Müraciətiniz qəbul olundu'
        message = 'Salam, dəyərli ' + str(applicant_name) + '. \nTezliklə sizinlə əlaqə saxlanılacaq.'
        from_email = settings.SERVER_EMAIL
        recipient_list = [applicant_email]
        send_mail(subject, message, from_email, recipient_list)
        if request.POST.get('email'):
            Applicant.objects.create(
                name = request.POST.get('name'),
                email = request.POST.get('email'),
    return render(request, 'pragmatechapp/frontend-development.html', context)

def backend(request):
    context = {
        'applicants': Applicant.objects.all()
    }
    if request.method == "POST":
        applicant_name = request.POST.get('name')
        applicant_email = request.POST.get('email')
        applicant_phone = request.POST.get('phone')
        subject = 'Müraciətiniz qəbul olundu'
        message = 'Salam, dəyərli ' + str(applicant_name) + '. \nTezliklə sizinlə əlaqə saxlanılacaq.'
        from_email = settings.SERVER_EMAIL
        recipient_list = [applicant_email]
        send_mail(subject, message, from_email, recipient_list)
        if request.POST.get('email'):
            Applicant.objects.create(
                name = request.POST.get('name'),
                email = request.POST.get('email'),
    return render(request, 'pragmatechapp/backend-development.html', context)

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