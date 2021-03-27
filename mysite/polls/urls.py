from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('student/<int:pk>/', views.DetailViewStudent.as_view(), name='detailStudent'),
    path('instructor/<int:pk>/', views.DetailViewInstructor.as_view(),
         name='detailInstructor'),
    path('meeting/<int:pk>/', views.MeetingView.as_view(), name='meeting'),
    path('meeting-list/',
         views.MeetingListView.as_view(), name='meeting-list'),
]
