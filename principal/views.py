from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect, render

def inicio(request):
    return render(request, 'principal/inicio.html')

@login_required
def dashboard_view(request):
    # Tu lógica del dashboard
    return render(request, 'principal/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('inicio')