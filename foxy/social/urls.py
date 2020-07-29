from django.urls import path

from social import views

urlpatterns = [
  path('home/', views.Home.as_view()),
  path('post/', views.Post.as_view()),
  path('post/<int:pk>/like', views.PostLike.as_view()),
  path('post/<int:pk>/comment', views.PostComment.as_view()),
  path('', views.Wall.as_view())
]
