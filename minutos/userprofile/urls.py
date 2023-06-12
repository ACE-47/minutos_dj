from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('login/',LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('my-account/',views.myaccount, name='my-account'),
    path('edit-profile/',views.edit_profile, name='edit-profile'),
    path('log-out/',LogoutView.as_view(), name='logout'),

]