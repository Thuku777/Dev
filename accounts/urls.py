from django.urls import path, include
from django.contrib.auth import views
from accounts import views

urlpatterns = [
    path('login/', views.user_login, name='user-login'),
    path('logout/', views.user_logout, name='user-logout'),
    path('register/', views.register, name='register'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),

    path('', include('django.contrib.auth.urls')),
]

