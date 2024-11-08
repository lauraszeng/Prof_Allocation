from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Professor(models.Model):
    # define category abbreviations
    VISITING_PROFESSOR = "Visiting Professor"
    LECTURER = "Lecturer on Law"
    #define category class
    CATEGORY = [
        (VISITING_PROFESSOR, "Visiting Professor"),
        (LECTURER, "Lecturer on Law")
    ]

    CATEGORY_LIST = ["Visiting Professor", "Lecturer on Law"]

    name = models.CharField(
        max_length=64
    )
    surname = models.CharField(
        max_length=64
    )
    position = models.CharField(
        max_length=64,
        choices=CATEGORY,
        default=LECTURER,
        blank=True
    )
    courses = models.ManyToManyField(
        'Course',
        blank=True,
        related_name='courseload'
    )

    def __str__(self):
        return f"{self.name} {self.surname}"
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "position": self.position,
            "course_id": [course.id for course in self.courses.all()],
            "course_names": [course.name for course in self.courses.all()],
            "course_credits": [course.credits for course in self.courses.all()]
        }

class Course(models.Model):
    name = models.CharField(
        max_length=500
    )
    credits = models.IntegerField()

    def __str__(self):
        return f"{self.name}"
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "credits": self.credits
        }
    
class Assistant(models.Model):
    name = models.CharField(
        max_length=64
    )
    surname = models.CharField(
        max_length=64
    )
    professor = models.ManyToManyField(
        'Professor',
        blank=True,
        related_name='assisting'
    )

    def __str__(self):
        return f"{self.name} {self.surname}"
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "professors": [professor.id for professor in self.professor.all()]
        }