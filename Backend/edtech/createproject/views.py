from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Projects, SubjectList, StudentLevel, ProjectForm
from .forms import CreateProjectForm
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from datetime import date

# Create your views here.
def index(request):
    project_list = Projects.objects.order_by('-Start_date')
    context = {'project_list': project_list}
    return render(request, 'createproject/index.html', context)


def keychecker(D, key):
    if key in D:
        return D[key]
    else:
        if 'date' in key:
            return date.fromisoformat('1970-01-01')
        else:
            return ''

def results(request):
    filters = request.GET
    if len(filters) == 0:
        project_list = Projects.objects.order_by('Start_date')
    else:
        project_list = Projects.objects.order_by('Start_date')\
                        .filter(Subjects__contains=keychecker(filters,'Subjects'),\
                        Level__contains=keychecker(filters,'Level'),\
                        Start_date__range= [keychecker(filters,'Start_date_0'),keychecker(filters,'Start_date_1')],\
                        )
                
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

    if form.is_valid():
        form.save()

    context['form'] = form
    return HttpResponseRedirect(reverse('createproject:results'))

def filter_projects(request):
    context = {}
    print(request.GET)

    return render(request,"results.html")