from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Classrooms, CreateClassForm
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
def create(request):
#     project_list = Projects.objects.order_by('-Start_date')
#     context = {'project_list': project_list}
    return render(request, 'createclass/create.html')

def results(request):
    #project_list = Projects.objects.order_by('-Start_date')
    #context = {'project_list': project_list}
    return render(request, 'createproject/results.html')


def create_new_class(request):
    context = {}
    form = CreateClassForm(request.POST or None)

    if form.is_valid():
        print(request.POST)
        form.save()

    context['form'] = form
    return HttpResponseRedirect(reverse('createclass:results'))