from django.http import HttpResponse
from django.shortcuts import render

def archive_year(request, year):
    return HttpResponse(f'{year}년도에 대한 내용')
