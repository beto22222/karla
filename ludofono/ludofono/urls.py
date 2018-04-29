from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from main.views import IndexView
from main.views import ServicesView
from main.views import ContactUsView
from main.views import GalleryView
from main.views import ProjectView
import main

from django.conf import settings
 
urlpatterns = [
    path('home/', IndexView.as_view(),name='home'),
    path('servicios/', ServicesView.as_view(),name='services'),
    
    path('contactanos/', ContactUsView.as_view(),name='contact_us'),
    path('galeria/', GalleryView.as_view(),name='gallery'),
    path('proyecto/', ProjectView.as_view(),name='proyecto'),
    path('send_email/', main.views.send_email,name='send_email'),
    path('admin/', admin.site.urls),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

