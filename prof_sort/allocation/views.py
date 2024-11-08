from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django.core import serializers
from .models import Professor, Course, Assistant
import json
from django import forms
from .forms import NewProfForm, NewCourseForm, NewAssistantForm

# Create your views here.

# generates data from models Professor, Course, and Assistant to be used in layout.html and index.html
def index(request):
    professors = Professor.objects.all()
    assistants = Assistant.objects.all()
    courses = Course.objects.all()
    return render(request, "allocation/index.html", {
        "professors": professors,
        "assistants": assistants,
        "courses": courses
    })

def professor_json(request, prof_id):
    # get dataset of specified prof
    professor = Professor.objects.get(pk=prof_id)
    # serialize prof info and return JsonResponse
    return JsonResponse(professor.serialize())

def course_json(request, course_id):
    # get dataset of specified course
    course = Course.objects.get(pk=course_id)
    # serialize course info and return JsonResponse
    return JsonResponse(course.serialize())

def assistant_json(request, assistant_id):
    # get dataset of specified assistant
    assistant = Assistant.objects.get(pk=assistant_id)
    # serialize assistant info and return JsonResponse
    return JsonResponse(assistant.serialize())

def add_prof(request):
    form = NewProfForm(request.POST)
    # follow this path is something has been posted
    if request.method == "POST":
        if form.is_valid():
            # if form is valid, pass the information into Professor model
            name = form.cleaned_data["name"]
            surname = form.cleaned_data["surname"]
            position = form.cleaned_data["position"]
            prof_courses = form.cleaned_data["courses"]
            new_prof = Professor.objects.create(
                name=name,
                surname=surname,
                position=position
            )
            # pass the courses into the prof model too
            for course in prof_courses:
                new_prof.courses.add(course)
            return render(request, "allocation/success.html")           
    return render(request, "allocation/add_prof.html", {
        "form": form
    })

def add_course(request):
    form = NewCourseForm(request.POST)
    # follow this path if something has been posted
    if request.method == "POST":
        if form.is_valid():
            # if form is valid, pass the information into Course model
            name = form.cleaned_data["name"]
            credits = form.cleaned_data["credits"]
            new_course = Course.objects.create(
                name=name,
                credits=credits
            )
            return render(request, "allocation/success.html")
    return render(request, "allocation/add_course.html", {
        "form": form
    })

def add_assistant(request):
    form = NewAssistantForm(request.POST)
    # follow this path if something has been posted
    if request.method == "POST":
        if form.is_valid():
            # if form is valid, pass the information into Assistant Model
            name = form.cleaned_data["name"]
            surname = form.cleaned_data["surname"]
            new_assistant = Assistant.objects.create(
                name=name,
                surname=surname
            )
            return render(request, "allocation/success.html")
    return render(request, "allocation/add_assistant.html", {
        "form": form
    })
