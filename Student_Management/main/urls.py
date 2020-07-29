from django.urls import path

from main import views

urlpatterns = [
  path('', views.Index.as_view()),
  path('college/<int:pk>', views.CollegeDetail.as_view(), name = 'college'),
  path('college/', views.CollegeList.as_view()),
  path('create_college/', views.CollegeCreate.as_view()),
  path('update_college/<int:pk>', views.CollegeUpdate.as_view()),
  path('create_student/', views.StudentCreate.as_view()),
  path('delete_student/<int:pk>', views.StudentDelete.as_view())
]
