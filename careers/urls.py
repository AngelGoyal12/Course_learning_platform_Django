from django.urls import path
from . import views

app_name = 'careers'

urlpatterns = [
    path('', views.careers_view, name='careers'),
    path('apply/', views.submit_application, name='submit_application'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('application/<int:application_id>/', views.application_detail, name='application_detail'),
]