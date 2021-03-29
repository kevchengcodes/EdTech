from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Projects, SubjectList, StudentLevel, ProjectForm
from .forms import CreateProjectForm
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
def index(request):
    project_list = Projects.objects.order_by('-Start_date')
    context = {'project_list': project_list}
    return render(request, 'createproject/index.html', context)

def results(request):
    project_list = Projects.objects.order_by('-Start_date')
    context = {'project_list': project_list}
    return render(request, 'createproject/results.html', context)

# class DetailView(generic.DetailView):
#     model = Projects
#     template_name = 'createproject/detail.html'
    
#     def get_queryset(self):
#         project_list = Projects.objects.order_by('-Start_date')
#         context = {'project_list': project_list}
#         return Projects.objects.filter(pub_date__lte=timezone.now())

# class ResultsView(generic.DetailView):
#     model = Projects
#     template_name = 'createproject/results.html'


def create_new_project(request):
    context = {}
    form = ProjectForm(request.POST or None)
    print(form)

    if form.is_valid():
        print(request.POST)
        form.save()

    context['form'] = form
    return HttpResponseRedirect(reverse('createproject:results'))