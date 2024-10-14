from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


#  /projects/ -> List of Projects
def projects(request):
    return HttpResponse('List of Projects')


# /project/1/ -> Single Project
def project(request, pk):
    return HttpResponse(f'A Single Project with id {pk}')
