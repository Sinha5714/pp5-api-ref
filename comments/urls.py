from django.urls import path
from comments import views

urlpatterns = [
    path('comments/', views.CommentListView.as_view()),

]
