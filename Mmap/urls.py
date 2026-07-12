from django.urls import path
from . import views

app_name = 'maps'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('select/', views.select_view, name='select'),
    path('edit/<int:map_id>/', views.edit_view, name='edit'),  # strからintに変更
    path('edit/<int:map_id>/save/', views.save_map_view, name='save_map'), # 保存用API
]