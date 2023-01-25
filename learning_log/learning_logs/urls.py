"""This is used to define the url log pattern for my app 'learning_logs'"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
        # App Home Page
        path('', views.index, name='index'),
        # This page diaplays all saved topics
        path('topics/', views.topics, name='topics'),
        # This page details entires of specific topics
        path('topics/<int:topic_id>/', views.topic, name='topic'),
        ]
