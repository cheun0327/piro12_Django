from django.http import HttpResponse
from django.shortcuts import render
from .models import Item

def archive_year(request, year):
    return HttpResponse(f'{year}년도에 대한 내용')

def item_lsit(request):
    qs=Item.objects.all()
    return render(request, 'blog/item_list.html', {
        'item_list':qs,
    })