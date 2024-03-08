from django.contrib import admin
from django.urls import path
from main_controller import views as main_controller_views
from emailsending import views as emailsending_views
from django.conf.urls import include

urlpatterns = [
    path('', main_controller_views.index, name='index'),
    path("main_controller/", include('main_controller.urls')),
    path("emailsending/",include("emailsending.urls")),
    path('admin/', admin.site.urls)
]