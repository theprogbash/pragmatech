from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about_us, name='about-us'),
    path('pragmatech-ustunlukler', views.advantages, name='pragmatech-ustunlukler'),
    path('tedris-paketleri', views.packages, name='tedris-paketleri'),
    path('pragmatech-qebul-prosesi', views.conditions, name='pragmatech-qebul-prosesi'),
    path('html-css', views.html_css, name='html-css'),
    path('javascript', views.javascript, name='javascript'),
    path('csharp', views.csharp, name='csharp'),
    path('php', views.php, name='php'),
    path('python', views.python, name='python'),
    path('software-deployment', views.software_deployment, name='software-deployment'),
    path('cybersecurity', views.cybersecurity   , name='cybersecurity'),
    path('foundation', views.foundation, name='foundation'),
    path('frontend-development', views.frontend, name='frontend-development'),
    path('backend-development', views.backend, name='backend-development'),
    path('contact', views.contact, name='contact'),
    path('coming_soon', views.coming_soon, name='coming_soon'),
]