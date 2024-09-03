from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('index/', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('menu_principal/', views.menu_principal, name='menu_principal'),
    path('mantenedor_masajes/', views.mantenedor_masajes, name='mantenedor_masajes'),
    path('crear_masaje/', views.crear_masaje, name='crear_masaje'),
    path('actualizar_masaje/<pk>/', views.actualizar_masaje, name='actualizar_masaje'),
    path('eliminar_masaje/<pk>/', views.eliminar_masaje, name='eliminar_masaje'),
]


