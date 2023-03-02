from django.urls import path
from . import views

app_name="passwordApp"

urlpatterns = [
    path('', views.home, name="home"),
    path('aboutus/', views.about, name="about"),
    path('password/', views.password, name="generatedpassword"),
]