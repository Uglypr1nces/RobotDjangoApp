from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from emailsending import views
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path("home/",views.home,name = "home"),
    path("information/",views.information,name = "information"),
    path("settings/",views.settings,name = "settings"),
    path('start/', views.start, name='start'),
    path('camera/', views.camera, name='camera'),
    path('sound/', views.sound, name='sound'),
    path('shutdown/', views.shutdown, name='shutdown'),
    path('savesettings/',views.savesettings,name = "savesettings"),
    path('Contact/', views.Contact, name='Contact'),
]
