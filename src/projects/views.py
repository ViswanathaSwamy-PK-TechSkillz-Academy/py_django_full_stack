from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


#  /projects/ -> List of Projects
def projects(request):
    return render(request, 'projects/projects.html')


# /project/1/ -> Single Project
def project(request, pk):
    return render(request, 'projects/single-project.html')
