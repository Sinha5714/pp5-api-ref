from django.urls import path
from . import views

urlpatterns = [
    path('join/', views.JoinListView.as_view()),
    path('join/<int:pk>/', views.JoinDetailView.as_view()),
]
