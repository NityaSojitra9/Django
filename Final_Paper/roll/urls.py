from django.urls import path
from . import views

urlpatterns = [
    path('', views.studentinfo, name='home'),
    path('welcome/', views.welcome, name='welcome'),
    path('search/', views.student_search, name='search'),
    path('info/<int:student_id>/', views.stuinformation, name='stuinformation'),
]
