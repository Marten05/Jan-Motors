from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),              # Home page
    path('category/', views.category, name='category'),  # Category page
    path('cart/', views.cart , name='cart'),          # Cart page
    path('about/', views.about, name='about'),        # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('profile/', views.profile, name='profile'),  # User profile page
    path('categories/exterior/', views.exterior, name='exterior'),  # Exterior category page
]