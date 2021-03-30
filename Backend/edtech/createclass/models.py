from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.
class Classrooms(models.Model):
    def __str__(self):
        return self.Name
    Name = models.CharField(max_length=255)
    Description = models.CharField(max_length=500)
    Subjects = models.CharField(max_length=255)
    Syllabus = models.TextField()
    Student_emails = models.TextField()


SUBJECTS = (
    ('ES','Environmental'),
    ('MA', 'Math'),
    ('B', 'Biology'),
    ('C', 'Chemistry'),
    ('P', 'Physics'),
    ('ME', 'Mechanical'),
    ('CS', 'Computer Science')
)
class CreateClassForm(ModelForm):
    Subjects = forms.MultipleChoiceField(choices = SUBJECTS)
    class Meta:
        model = Classrooms
        fields = '__all__'
