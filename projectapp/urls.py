from django.urls import path

from projectapp.views import ProjectListView, ProjectCreateView, ProjectDetailView

app_name = 'projectapp'

urlpatterns =[
     path('list/', ProjectListView.as_view(),name='list'),

     path('create/', ProjectCreateView.as_view(), name='list'),
     path('detail/', ProjectDetailView.as_view(), name='list'),

]