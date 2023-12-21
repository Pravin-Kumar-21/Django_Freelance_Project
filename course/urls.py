from . import views
from django.urls import path, include


app_name = "course"
urlpatterns = [path("list/", views.CourseList.as_view(), name="course")]
