from django.urls import path
from app import views
urlpatterns=[
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('team',views.team,name='team'),
    path('why',views.why,name='why'),
    path('login',views.login,name='login'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('testmonial',views.testmonial,name='testmonial'),
    path('add',views.add,name='add'),
]