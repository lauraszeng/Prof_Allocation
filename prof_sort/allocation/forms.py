from django import forms
from django.forms import ModelForm
from .models import Professor, Course, Assistant

class NewProfForm(ModelForm):
    class Meta:
        model = Professor
        fields = ("name", "surname", "position", "courses")

class NewCourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ("name", "credits")

class NewAssistantForm(ModelForm):
    class Meta:
        model = Assistant
        fields = ("name", "surname")