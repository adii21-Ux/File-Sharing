from django.urls import path, include
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('profile', profile, name="profile"),
    path('profile/<str:username>/', user_profile, name='user_profile'),
    path('login', login, name="login"),
    path('logout', logout_user, name="logout"),
    path('register', register, name="register"),
    path('upload', file_upload, name='file_upload'),
    path('files', file_list, name='file_list'),
    path('download/<int:file_id>/', download_file, name='download_file'),
    path('search', search_profiles, name='search'),

    path('share/<int:file_id>/', share_file, name='share_file')
]