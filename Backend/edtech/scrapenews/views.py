from django.shortcuts import render
from django.http import HttpResponse
from .models import NewsList

# Create your views here.
def index(request):
    latest_news_list = NewsList.objects.order_by('-Date')
    context = {'latest_news_list': latest_news_list}
    return render(request, 'scrapenews/index.html', context)