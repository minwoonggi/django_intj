from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DeleteView, DetailView

from projectapp.decorators import project_ownership_required
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 20

class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'
    success_url = reverse_lazy('articleapp:list')

    # def get_success_url(self):
    #     return reverse('projectapp:detail', kwargs={'pk':self.object.pk})

@method_decorator(project_ownership_required, 'get')
@method_decorator(project_ownership_required, 'post')
class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projectapp/delete.html'