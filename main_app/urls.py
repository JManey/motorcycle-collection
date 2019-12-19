from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('motorcycles/', views.motorcycles_index, name='index'),
  path('motorcycles/<int:motorcycle_id>/', views.motorcycles_detail, name='detail'),
  path('motorcycles/create/', views.MotorcycleCreate.as_view(), name='motorcycles_create'),
  path('motorcycles/<int:pk>/update/', views.MotorcycleUpdate.as_view(), name='motorcycles_update'),
  path('motorcycles/<int:pk>/delete/', views.MotorcycleDelete.as_view(), name='motorcycles_delete'),
  path('motorcycles/<int:motorcycle_id>/assoc_acc/<int:acc_id>/', views.assoc_acc, name='assoc_acc'),
  path('motorcycles/<int:motorcycle_id>/unassoc_acc/<int:acc_id>/', views.unassoc_acc, name='unassoc_acc'),
  path('motorcycles/<int:motorcycle_id>/add_photo/', views.add_photo, name='add_photo'),
  path('accs/', views.AccList.as_view(), name='accs_index'),
  path('accs/<int:pk>/', views.AccDetail.as_view(), name='accs_detail'),
  path('accs/create/', views.AccCreate.as_view(), name='accs_create'),
  path('accs/<int:pk>/update/', views.AccUpdate.as_view(), name='accs_update'),
  path('accs/<int:pk>/delete/', views.AccDelete.as_view(), name='accs_delete'),
  path('accounts/signup', views.signup, name='signup'),
]