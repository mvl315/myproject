from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index ),
    path('page', views.page),
    path('about', views.about),
    path('contracts', views.contracts),
    path('custom', views.custom),
    path('profile', views.profile),
    path('registr', views.registr)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)