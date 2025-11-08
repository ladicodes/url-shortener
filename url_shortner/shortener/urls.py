from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Dashboard/home page
    path('<str:short_id>/', views.redirect_short_url, name='redirect_url'),  # Redirect short URLs
]
