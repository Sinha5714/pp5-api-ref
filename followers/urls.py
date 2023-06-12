"""
A module for urls in the followers app
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path

# Internal:
from followers import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

urlpatterns = [
    path('followers/', views.FollowerListView.as_view()),
    path('followers/<int:pk>/', views.FollowerDetailView.as_view()),
]
