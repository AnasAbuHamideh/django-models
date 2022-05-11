from django.urls import path
from .views import SnackListView,HomeView,SnackDetailView

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('snacks-list',SnackListView.as_view(), name= 'snacks-list'),
    path('detail-snack/<int:pk>',SnackDetailView.as_view(), name='snacks-detail')
]