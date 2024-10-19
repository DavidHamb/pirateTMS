from django.shortcuts import render
from tms.models import Target

# Create your views here.

def targets(request):
    targets = Target.objects.all()

    return render(request, 'tms/targets.html', {'targets' : targets})
