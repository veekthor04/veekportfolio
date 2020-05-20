from django.shortcuts import render
from veekprojects.models import Project

# Create your views here.
def project_index(request):
    projects = Project.objects.all()
    contexts = {
        'projects' : projects
    }
    return render(request, 'project_index.html', contexts)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
