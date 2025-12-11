from django.urls import path
from . import views

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),
    path('about/', views.about_page, name='about'),
    path('projects/', views.projects_page, name='projects'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('certificates/', views.certificates_page, name='certificates'),
    path('contact/', views.contact_page, name='contact'),
]
