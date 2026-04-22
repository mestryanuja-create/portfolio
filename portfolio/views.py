from django.views import View
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def project_list(request):
    project = Project.objects.all()
    context = {'project_list':project}
    return render(request,"portfolio/project_list.html",context)

class ProjectDeleteView(LoginRequiredMixin, View):

    def get(self, request, pk=None):
        project = Project.objects.get(pk=pk)
        return render(request, "portfolio/delete_project.html", {'project': project})

    def post(self, request, pk=None):
        project = Project.objects.get(pk=pk)
        project.delete()
        return redirect('portfolio_list')

class ProjectCreateView(LoginRequiredMixin, View):
    template_name = ''

    def get(self, request):
        form = ProjectForm()
        return render(request, "portfolio/add_project.html", {'form': form})

    def post(self, request):
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio_list')  # Redirect to the portfolio list view
        return render(request, "portfolio/project_list.html", {'form': form})

class ProjectEditView(LoginRequiredMixin, View):


    def get(self, request, pk=None):
        project = Project.objects.get(pk=pk)
        form = ProjectForm(instance=project)
        return render(request, "portfolio/edit_project.html", {'form': form})

    def post(self, request, pk=None):
        project = Project.objects.get(pk=pk)
        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            return redirect('portfolio_list')  # Redirect to the portfolio list view

        return render(request, "portfolio/project_list.html", {'form': form})
