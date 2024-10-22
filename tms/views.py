from django.shortcuts import render, redirect
from tms.models import Target
from tms.forms import TargetForm

# Create your views here.

def targets(request):
    targets = Target.objects.all()
    return render(request, 'tms/targets.html', {'targets' : targets})


def target_detail(request, id):
    target = Target.objects.get(id=id)
    return render(request, 'tms/target_detail.html', {'target': target})


def targets_add(request):
    if request.method == 'POST':
        form = TargetForm(request.POST)
        if form.is_valid():
            target = form.save()
            return redirect('target-detail', target.id)
    else: 
        form = TargetForm()

    return render(request, 'tms/targets_add.html', {'form': form})


def target_update(request, id):
    target = Target.objects.get(id=id)

    if request.method == "POST":
        form = TargetForm(request.POST, instance=target)
        if form.is_valid:
            form.save()
            return redirect('target-detail', target.id)
    else: 
        form = TargetForm(instance=target)

    return render(request, 'tms/target_update.html', {'form':form})


def target_delete(request, id):
    target = Target.objects.get(id=id)

    if request.method == 'POST':
        target.delete()
        return redirect('targets')
        
    return render(request, 'tms/target_delete.html', {'target':target})






