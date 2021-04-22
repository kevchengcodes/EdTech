from django.shortcuts import render
from django.http import HttpResponse
from .models import PostList, PostForm, ProjPostList, ProjPostForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime

# Create your views here.
def createpost(request):
    context = {}
    form = PostForm(request.POST or None)
    print(form)
    #form['DateClicked'] = datetime.today().strftime('%Y/%m/%d')

    if form.is_valid():
        obj = form.save(commit=False)
        obj.PostDate = datetime.now()
        obj.save()

    context['form'] = form
    return HttpResponseRedirect(reverse('scrapenews:index'))

def createprojpost(request):
    context = {}
    form = ProjPostForm(request.POST or None)
    print(form)
    #form['DateClicked'] = datetime.today().strftime('%Y/%m/%d')

    if form.is_valid():
        obj = form.save(commit=False)
        obj.PostDate = datetime.now()
        obj.save()

    context['form'] = form
    return HttpResponseRedirect(reverse('createproject:proj_detail', kwargs={'proj_id': obj.ProjKey}))