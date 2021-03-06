from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import logging
from shop.models import Item


def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))

def item_list(request):
    qs=Item.objects.all()
    q=request.GET.get('q', '')
    if q:
        qs=qs.filter(name_icontains=q)

    return render(request, 'shop/item_list.html', {
        'item_list':qs,
        'q':q,
    })

def item_detail(request, pk):
    item=get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_deatil.html', {'item':item,})

def item_new(request):
    print('GET :', request.GET)
    print('POST :', request.POST)
    print('FILES :', request.FILES)
    return render(request, 'shop/item_form.html')