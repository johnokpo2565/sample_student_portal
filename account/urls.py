from  django.urls import path, include
from . import views

app_name = "account"

urlpatterns = [
    path('',views.home, name="home"),
    path('<uuid:pk>/profile/',views.profile, name="profile"),
    path('<uuid:pk>/update_profile/',views.update_profile, name="update_profile"),
]