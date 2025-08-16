from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path("__reload__/", include("django_browser_reload.urls")),
    
]

