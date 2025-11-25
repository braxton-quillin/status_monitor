from django.shortcuts import render
from .models import Appliance 

def dashboard(request):
    appliances = Appliance.objetcs.all()
    return render(request, 'dashboard.html', {'appliances': appliances})

# views.py
from django.shortcuts import render, redirect
from .forms import ApplianceForm

def add_appliance(request):
    if request.method == 'POST':
        form = ApplianceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # redirect to your dashboard view
    else:
        form = ApplianceForm()
    return render(request, 'add_appliance.html', {'form': form})
