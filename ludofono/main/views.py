from django.shortcuts import render
from django.views.generic import TemplateView


from django.http import HttpResponseRedirect
import json
import requests 
import smtplib




# Create your views here.
class IndexView(TemplateView):

    template_name='main/index.html'

    
class ServicesView(TemplateView):

    template_name='main/services.html'
    
class ContactUsView(TemplateView):

    template_name='main/contact_us.html'
    
class GalleryView(TemplateView):

    template_name='main/gallery.html'

class ProjectView(TemplateView):

    template_name='main/proyecto.html'


def send_email(request):

    print("----------------------------------------------")
    
    msg = request.GET.get('name') + " > " + request.GET.get('email') + " dice: " + request.GET.get('content')
    print(msg)
    print("mensaje enviado")
    fromaddr = 'alberto.moca12350@gmail.com'
    toaddrs  = 'albeam12350@gmail.com'
     
    # Datos
    username = 'alberto.moca12350@gmail.com'
    password = 'elhijodelinternet'
     
    # Enviando el correo
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)

    BODY = '\r\n'.join(['To: %s' % toaddrs,
                    'From: %s' % fromaddr,
                    'Subject: %s' % "SUBJECT",
                    '', msg])
    try:
        server.sendmail(fromaddr, toaddrs, BODY)
        print ('email sent')
    except:
        print ('error sending mail')
    return(HttpResponseRedirect('/'))



    server.quit()
