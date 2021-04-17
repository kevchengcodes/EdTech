from django.db import models
from django.core.validators import int_list_validator
from django.forms import ModelForm
from django import forms

# Create your models here...
class Projects(models.Model):
    def __str__(self):
        return self.Title
    Title = models.TextField()
    Short = models.TextField()
    Long = models.TextField() 
    #Image = models.FileField()
    #Image_data = models.BinaryField(null=True)
    Subjects = models.CharField(max_length=255)
    Class_size = models.TextField() 
    Group_size = models.TextField() 
    Level = models.CharField(max_length=255)
    Hours_estimated = models.IntegerField()
    Virtual = models.TextField()
    Locations = models.CharField(max_length=255)
    Start_date = models.DateField(blank=True, null=True)
    End_date = models.DateField(blank=True, null=True)
    Partner = models.CharField(max_length=255, default='GeorgiaTech')
    ClassNum = models.IntegerField(default=0)

class SubjectList(models.Model):
    def __str__(self):
        return self.Name
    Name = models.CharField(max_length=255)
    Abbreviation = models.CharField(max_length=3)

class StudentLevel(models.Model):
    def __str__(self):
        return self.Level
    Level = models.CharField(max_length=255)
    Abbreviation = models.CharField(max_length=3)

LEVELS = (
    ('E','Elementary'),
    ('M', 'Middle'),
    ('H', 'High'),
    ('U', 'Undergrad'),
    ('G', 'Grad'),
)
SUBJECTS = (
    ('ES','Environmental'),
    ('MA', 'Math'),
    ('B', 'Biology'),
    ('C', 'Chemistry'),
    ('P', 'Physics'),
    ('ME', 'Mechanical'),
    ('CS', 'Computer Science')
)
# Model Forms
class ProjectForm(ModelForm):
    Level = forms.MultipleChoiceField(choices = LEVELS)
    Subjects = forms.MultipleChoiceField(choices = SUBJECTS)
    class Meta:
        model = Projects
        fields = '__all__'#['Title','Short','Long','Image','Image_data','Subjects','Class_size','Group_size','Level','Hours_estimated','Virtual','Locations','Start_date','End_date']