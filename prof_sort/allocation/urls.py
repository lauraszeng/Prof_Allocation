from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_prof", views.add_prof, name="add_prof"),
    path("add_course", views.add_course, name="add_course"),
    path("add_assistant", views.add_assistant, name="add_assistant"),
    # API URLs
    path("professor_json/<int:prof_id>", views.professor_json, name="professor_json"),
    path("course_json/<int:course_id>", views.course_json, name="course_json"),
    path("assistant_json/<int:assistant_id>", views.assistant_json, name="assistant_json")
]
