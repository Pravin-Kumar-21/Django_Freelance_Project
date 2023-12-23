# forms.py

from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "instructor",
            "capacity",
            "open_seats",
        )
