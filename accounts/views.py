from django.shortcuts import render 
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def index(request,):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        email_content = render_to_string('email_template.html', {'username': username})
        send_mail('submitted succesfully',
                  username,
                  'settings.EMAIL_HOST_USER',
                  [email],
                  fail_silently=False,
                   html_message=email_content )
    return render(request,'index.html') 