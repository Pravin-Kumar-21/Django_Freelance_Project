from django.views.generic import ListView
from . import models
from django.shortcuts import render


class CourseList(ListView):
    model = models.Students
    template_name = "templates/course_list.html"

    def get(self, request):
        return render(request, "course_list.html")


def course_list(request):
    courses = models.Students.objects.all()
    return render(request, "course_list.html", {"courses": courses})
