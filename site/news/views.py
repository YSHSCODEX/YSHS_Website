from django.shortcuts import render, get_object_or_404
from .models import contents

def index(request):
    news_list = contents.objects.order_by('-create_date')
    context = {'news_list': news_list}
    return render(request, 'news/news_list.html ')

def detail(request,contents_id):
    contents = get_object_or_404(contents, pk=contents_id)
    context = {'contents': contents}
    return render(request, 'news/contents_detail.html', context)