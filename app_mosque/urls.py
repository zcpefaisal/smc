from django.urls import path
from app_mosque import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),

]