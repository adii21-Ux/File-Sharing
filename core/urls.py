from django.urls import path, include
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('profile', home, name="profile"),
    path('login', login, name="login"),
    path('logout', logout_user, name="logout"),
    path('register', register, name="register"),
    path('upload', file_upload, name='file_upload'),
]