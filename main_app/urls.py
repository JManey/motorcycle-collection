from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('motorcycles/', views.motorcycles_index, name='idex'),
  path('motorcycles/<int:motorcycle_id>/', views.motorcycles_detail, name='detail'),
]