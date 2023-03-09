from django.shortcuts import render,redirect
from .form import RegistrationForm
from  django.contrib.sites.shortcuts import get_current_site
import random
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

from .models import Registration


# Create your views here.

def home(request):
    return render(request,'home.html')

def RegisterationView(request):
    form = RegistrationForm()
    if request.method == 'POST':
        username = request.POST.get('uname')
        email = request.POST.get('email')
        # print(email)
        # print(type(email))
        user = Registration(uname=username,email=email)

        domain_name = get_current_site(request).domain
        token = str(random.random()).split('.')[1]

        user.token =token

        link = f'http://{domain_name}/verify/{token}'

        send_mail(
            'Email Verification',
            f'Please click {link} to verify your email!',
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False,
        )
        return HttpResponse('The mail has been sent')

    return render(request,'register.html',{'form':form})

def verify(request, token):
    try:
        user = Registration.objects.filter(token = token)
        if user:
            user.is_verified = True
            msg = 'Your email has been verified'
            print(msg)
        return redirect('home')

    except Exception as e:
        msg = e
        return render(request,'info.html',{'msg': e})
