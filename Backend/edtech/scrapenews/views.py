from django.shortcuts import render
from django.http import HttpResponse
from .models import NewsList, ArticlesClickedForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime

# Create your views here.
def index(request):
    latest_news_list = NewsList.objects.order_by('Link','-Date').distinct('Link')
    context = {'latest_news_list': latest_news_list}
    return render(request, 'scrapenews/index.html', context)

def log_link(request):
    context = {}
    form = ArticlesClickedForm(request.POST or None)
    #form['DateClicked'] = datetime.today().strftime('%Y/%m/%d')
    print(form)

    if form.is_valid():
        form.save()

    context['form'] = form
    return HttpResponseRedirect(reverse('scrapenews:index'))