from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Classrooms, CreateClassForm
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from createproject.models import Projects
from addpost.models import PostList

# Create your views here.
def index(request):
#     project_list = Projects.objects.order_by('-Start_date')
#     context = {'project_list': project_list}
    return render(request, 'createclass/index.html')

def home(request):
    project_list = Projects.objects.filter(ClassNum = 1).order_by('-Start_date')
    latest_posts = PostList.objects.order_by('-PostDate')[0:30]
    context = {'project_list': project_list, 'latest_posts': latest_posts}
    return render(request, 'createclass/home.html', context)


def create_new_class(request):
    context = {}
    form = CreateClassForm(request.POST or None)

    print(form)
    if form.is_valid():
        form.save()

    context['form'] = form
    return HttpResponseRedirect(reverse('createclass:home'))

def deletepost(request, post_id):
    post = get_object_or_404(PostList, pk=post_id)
    post.delete()

    return HttpResponseRedirect(reverse('createclass:home'))

def removeproj(request, proj_id):
    proj = get_object_or_404(Projects, pk=proj_id)
    proj.ClassNum = 0
    proj.save()

    return HttpResponseRedirect(reverse('createclass:home'))