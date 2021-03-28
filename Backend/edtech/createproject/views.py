from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Projects, SubjectList, StudentLevel, ProjectForm
from .forms import CreateProjectForm
from django.urls import reverse

# Create your views here.
def index(request):
    project_list = Projects.objects.order_by('-Start_date')
    context = {'project_list': project_list}
    return render(request, 'createproject/index.html', context)


def create_new_project(request):
    context = {}
    form = ProjectForm(request.POST or None)
    print(form)

    if form.is_valid():
        print(request.POST)
        form.save()

    context['form'] = form
    return render(request, 'createproject/index.html', context)