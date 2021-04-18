from django.shortcuts import render
from django.http import HttpResponse
from .models import NewsList, ArticlesClickedForm
from addpost.models import PostList
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime

# Create your views here.
def index(request):
    for Link in NewsList.objects.values_list('Link', flat=True).distinct():
        NewsList.objects.filter(pk__in=NewsList.objects.filter(Link=Link).values_list('id', flat=True)[1:]).delete()
    latest_news_list = NewsList.objects.order_by('-Date')[0:30]
    latest_posts = PostList.objects.order_by('-PostDate')[0:30]
    context = {'latest_news_list': latest_news_list, 'latest_posts': latest_posts}
    return render(request, 'scrapenews/index.html', context)

def index2(request):
    for Link in NewsList.objects.values_list('Link', flat=True).distinct():
        NewsList.objects.filter(pk__in=NewsList.objects.filter(Link=Link).values_list('id', flat=True)[1:]).delete()
    latest_news_list = NewsList.objects.order_by('-Date')[0:30]
    latest_posts = PostList.objects.order_by('-PostDate')[0:30]
    context = {'latest_news_list': latest_news_list, 'latest_posts': latest_posts}
    
    return render(request, 'scrapenews/index2.html', context)

def log_link(request):
    context = {}
    form = ArticlesClickedForm(request.POST or None)
    #form['DateClicked'] = datetime.today().strftime('%Y/%m/%d')

    if form.is_valid():
        form.save()

    context['form'] = form
    return HttpResponseRedirect(reverse('scrapenews:index'))

def cognitive_questionnaire(request):
    return render(request, 'scrapenews/cognitive.html')

def cognitivehome(request):
    answers = request.GET
    fi = 0
    fd = 0
    print(answers)
    for key in answers:
        if answers[key] == "fi":
            fi += 1
        else:
            fd += 1
    
    if fi > fd:
        print('going to fi page', fd, fi)
        return HttpResponseRedirect(reverse('scrapenews:index'))
    else:
        print('going to fd page', fd, fi)
        return HttpResponseRedirect(reverse('scrapenews:index2'))