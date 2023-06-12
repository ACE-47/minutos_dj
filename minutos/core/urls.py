
from django.urls import path
from . import views
urlpatterns = [
    path('',views.frontpage, name='frontpage'),
    path('privecy-policy/',views.privecy, name='privecy-policy'),
    path('terms/',views.terms, name='terms'),
    path('plans/',views.plans, name='plans'),



]
