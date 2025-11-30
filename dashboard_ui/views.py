from django.shortcuts import render, redirect
from Smart_Load_Health_Monitor.models import Appliance
from .forms import ApplianceForm

def home(request):
    return redirect('dashboard')

def ui(request):
    appliances = Appliance.objects.all()
    return render(request, 'ui.html', {'appliances': appliances})

def add_appliance(request):
    if request.method == 'POST':
        form = ApplianceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # redirect to your dashboard view
    else:
        form = ApplianceForm()
    return render(request, 'add_appliance.html', {'form': form})
