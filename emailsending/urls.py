from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('Contact/',views.Contact,name="Contact"),
    path('send_email', views.send_email, name='send_email'),
    path('', views.index, name='index')
]
