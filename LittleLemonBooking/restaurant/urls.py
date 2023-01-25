from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]