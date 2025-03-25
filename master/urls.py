from django.urls import path
from . import views


urlpatterns = [

    path('task/',views.TaskAPI.as_view()),
    path('assign_task/',views.AssignTaskAPI.as_view()),
    path('user_task/',views.UserTaskAPI.as_view()),
]