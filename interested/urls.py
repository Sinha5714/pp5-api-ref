"""
A module for urls in the intererested app
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path

# Internal:
from interested import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

urlpatterns = [
    path('interested/', views.InterestedListView.as_view()),
    path('interested/<int:pk>/', views.InterestedDetailView.as_view()),
]
