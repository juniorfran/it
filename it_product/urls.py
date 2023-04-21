from django.urls import path
from . import views


urlpatterns = [
    path('product_list', views.product_list, name='product_list'),
    path('product_create', views.product_create, name='product_create'),
    path('product_create', views.product_view, name='product_view'),
    # path('product_create', views.tabla_lista_produtos, name='paginacion_tabla'),
    path('product_edit/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('product_delete/<int:pk>/delete/', views.product_delete, name='product_delete'),

]