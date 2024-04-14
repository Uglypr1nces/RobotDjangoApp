from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #pages
    path('', views.index, name=''),
    path("home/",views.home,name = "home"),
    path("information/",views.information,name = "information"),
    path("settings/",views.settings,name = "settings"),
    #robot features
    path('camera/', views.camera, name='camera'),
    path('sound/', views.sound, name='sound'),
    path('shutdown/', views.shutdown, name='shutdown'),
    path('savesettings/',views.savesettings,name = "savesettings"),
    path("sendmessage/",views.sendmessage,name = "sendmessage"),
    #robot bodymovement
    path("forward/",views.forward,name = "forward"),
    path("backward/",views.backward,name = "backward"),
    path("left/",views.left,name = "left"),
    path("right/",views.right,name = "right"),
    #robot camera movement
    path("camera_left/",views.camera_left,name = "camera_left"),
    path("camera_right/",views.camera_right,name = "camera_right"),
    path("camera_up/",views.camera_up,name = "camera_up"),
    path("camera_down/",views.camera_down,name = "camera_down"),
]
