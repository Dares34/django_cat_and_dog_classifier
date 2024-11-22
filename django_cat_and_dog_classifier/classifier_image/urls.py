from django.urls import path, include
from .views import upload_image
from . import views

urlpatterns = [
    path('upload_image/', name = 'upload_image'),
]