from django.contrib import admin
from django.urls import path
from main_controller import views as main_controller_views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', main_controller_views.index, name='index'),
    path("main_controller/", include('main_controller.urls')),
    path('admin/', admin.site.urls)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)