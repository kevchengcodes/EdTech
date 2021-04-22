from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Projects, SubjectList, StudentLevel, ProjectForm
from addpost.models import ProjPostList
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
                        Partner__contains=keychecker(filters,'Partner'),\
                        Level__contains=keychecker(filters,'Level'),\
                        Start_date__range= [keychecker(filters,'Start_date_0'),keychecker(filters,'Start_date_1')],\
                        )
                
    context = {'project_list': project_list}
    return render(request, 'createproject/results.html', context)

def addprojtoclass(request, proj_id):
    proj = get_object_or_404(Projects, pk=proj_id)
    proj.ClassNum = 1
    proj.save()

    return HttpResponseRedirect(reverse('createclass:home'))

def create_new_project(request):
    context = {}
    form = ProjectForm(request.POST or None)
    print(form)

    if form.is_valid():
        print(form)
        form.save()

    context['form'] = form
    return HttpResponseRedirect(reverse('createproject:home'))

def home(request):
    project_list = Projects.objects.order_by('-Start_date').filter(Partner='KevinCo')
    context = {'project_list': project_list}
    return render(request, 'createproject/partner_home.html', context)

def proj_detail(request, proj_id):
    proj = get_object_or_404(Projects, pk=proj_id)
    latest_posts = ProjPostList.objects.filter(ProjKey=proj_id).order_by('-PostDate')[0:30]
    context = {}
    context['proj'] = proj
    context['latest_posts'] = latest_posts

    return render(request, 'createproject/proj_detail.html', context)
