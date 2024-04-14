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
    path('camera/', views.camera, name='camera'),
    path('sound/', views.sound, name='sound'),
    path('shutdown/', views.shutdown, name='shutdown'),
    path('savesettings/',views.savesettings,name = "savesettings"),
    path('Contact/', views.Contact, name='Contact'),
    path("sendmessage/",views.sendmessage,name = "sendmessage"),
    path("forward/",views.forward,name = "forward"),
    path("backward/",views.backward,name = "backward"),
    path("left/",views.left,name = "left"),
    path("right/",views.right,name = "right"),
    path("camera_left/",views.camera_left,name = "camera_left"),
    path("camera_right/",views.camera_right,name = "camera_right"),
    path("camera_up/",views.camera_up,name = "camera_up"),
    path("camera_down/",views.camera_down,name = "camera_down"),
]
