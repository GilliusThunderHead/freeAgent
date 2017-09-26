from django.http import HttpResponse
from .models import Project, Review
from django.shortcuts import render, get_object_or_404


#Returns all projects
def index(request):   
    all_projects=Project.objects.all()
    return render(request,'freeAgentApp/index.html', { 'all_projects':all_projects })
  
  
#Returns project details    
def detail(request,project_id):   
    project_detail=get_object_or_404(Project, pk=project_id)
    return render(request,'freeAgentApp/detail.html', {'project_detail':project_detail})
 
    