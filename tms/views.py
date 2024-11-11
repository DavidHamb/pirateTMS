from django.shortcuts import render, redirect
from tms.models import Target, Note, Vulnerability, Ressource
from tms.forms import TargetForm, NoteForm, VulnerabilityForm, RessourceForm
from django.contrib import messages
from datetime import date

# Create your views here.

def targets(request):
    targets = Target.objects.all()
    targets = targets.order_by('-last_update').values()
    return render(request, 'tms/targets.html', {'targets' : targets})


def target_detail(request, id):
    target = Target.objects.get(id=id)
    notes = Note.objects.filter(linked_target=target.id)
    notes = notes.order_by('-id').values()
    return render(request, 'tms/target_detail.html', {'target': target, 'notes':notes})


def targets_add(request):
    if request.method == 'POST':
        form = TargetForm(request.POST)
        if form.is_valid():
            target = form.save()
            messages.add_message(request, messages.INFO, "A new target has been successfully created! You can now edit the details ...")
            return redirect('target-detail', target.id)
    else: 
        form = TargetForm()

    return render(request, 'tms/targets_add.html', {'form': form})


def target_update(request, id):
    target = Target.objects.get(id=id)

    if request.method == "POST":
        form = TargetForm(request.POST, instance=target)
        if form.is_valid:
            target.last_update = date.today()
            target.save()
            form.save()
            messages.add_message(request, messages.INFO, "The target has been successfully updated ...")
            return redirect('target-detail', target.id)
    else: 
        form = TargetForm(instance=target)

    return render(request, 'tms/target_update.html', {'form':form})



def target_delete(request, id):
    target = Target.objects.get(id=id)

    if request.method == 'POST':
        target.delete()
        messages.add_message(request, messages.INFO, "The target has been deleted ...")
        return redirect('targets')

    return render(request, 'tms/target_delete.html', {'target':target})



def add_note(request, id):
    target = Target.objects.get(id=id)
    form = NoteForm()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():

            # Save form data AND the linked target (as hidden value)
            temporary_completion = form.save(commit=False)
            temporary_completion.linked_target = target
            temporary_completion.save()
            target.last_update = date.today()
            target.save()
            return redirect('target-detail', target.id)
    else:
        form = NoteForm()

    return render(request, 'tms/add_note.html', {'form': form, 'target': target}) 



def delete_note(request, id):
    note = Note.objects.get(id=id)
    target = Target.objects.get(id=note.linked_target_id)

    if request.method == 'POST':
        target.last_update = date.today()
        target.save()
        note.delete()
        messages.add_message(request, messages.INFO, "The note has been deleted ...")
        return redirect('target-detail', target.id)
    
    return render(request, 'tms/delete_note.html', {'note': note, 'target': target})


def vulnerabilities(request):
    vulnerabilities = Vulnerability.objects.all()

    if request.method == 'POST':
        search_query = request.POST['search_query']
        vulnerabilities =  Vulnerability.objects.filter(name__contains=search_query) | Vulnerability.objects.filter(description__contains=search_query) | Vulnerability.objects.filter(cve__contains=search_query) | Vulnerability.objects.filter(category__contains=search_query) 
        vulnerabilities = vulnerabilities.order_by('-id').values()
        return render(request, 'tms/vulnerabilities.html', {'vulnerabilities': vulnerabilities, 'query': search_query})
    
    vulnerabilities = vulnerabilities.order_by('-id').values()
    return render(request, 'tms/vulnerabilities.html', {'vulnerabilities' : vulnerabilities})



def vulnerabilities_add(request):
    if request.method == 'POST':
        form = VulnerabilityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "A new vulnerability has been added ...")
            return redirect('vulnerabilities')
    else: 
        form = VulnerabilityForm()

    return render(request, 'tms/vulnerabilities_add.html', {'form': form})


def ressources(request):
    ressources = Ressource.objects.all()
    return render(request, 'tms/ressources.html', {'ressources' : ressources})


def ressources_add(request):
    if request.method == 'POST':
        form = RessourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ressources')
    else: 
        form = RessourceForm()

    return render(request, 'tms/ressources_add.html', {'form': form})


def checklist(request):
    return render(request, 'tms/checklist.html')
