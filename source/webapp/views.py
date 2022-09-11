from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Project, STATUS_CHOICES


def index_view(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'index.html', context)


def task_view(request,  *args, **kwargs):
    pk = kwargs.get('pk')
    project =  Project.objects.get(pk=pk)
    return render(request,'task_view.html', {'project': project})


def create_task(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'create_task.html', {'statuss':STATUS_CHOICES})
    elif request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        create_add = request.POST.get('create_add')
        new_project = Project.objects.create(description=description, status=status, create_add=create_add)

        return redirect('task_view', pk=new_project.pk)
