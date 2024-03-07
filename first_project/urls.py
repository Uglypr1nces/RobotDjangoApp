from django.contrib import admin
from django.urls import path
from first_app import views as first_app_views
from emailsending import views as emailsending_views
from django.conf.urls import include

urlpatterns = [
    path('', first_app_views.index, name='index'),
    path("first_app/", include('first_app.urls')),
    path("emailsending/",include("emailsending.urls")),
    path('admin/', admin.site.urls)
]