from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),              # Home page
    path('category/', views.category, name='category'),  # Category page
    path('cart/', views.cart , name='cart'),          # Cart page
    path('about/', views.about, name='about'),        # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('profile/', views.profile, name='profile'),  # User profile page
    path('categories/exterior/', views.exterior, name='exterior'),  # Exterior category page
    path('categories/interior/', views.interior, name='interior'),  # Interior category page
    path('categories/maintenance/', views.maintenance, name='maintenance'),  # Maintenance category page
    path('categories/accessories/', views.accessories, name='accessories'),  # accessories category page
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)