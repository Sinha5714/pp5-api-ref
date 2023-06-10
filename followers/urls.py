from django.urls import path
from followers import views

urlpatterns = [
    path('followers/', views.FollowerListView.as_view()),
]
