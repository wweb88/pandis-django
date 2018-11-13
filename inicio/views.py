from django.shortcuts import redirect
from django.shortcuts import render
from .models import Luchador
from .forms import RegistroForm

# Create your views here.
def home(request):
	e = Luchador.objects.all()
	return render(request, 'inicio/home.html',{'luchadores' : e})


def luchadores(request):
	e = Luchador.objects.all()
	return render(request, 'inicio/miembros.html',{'luchadores' : e})



def inscripcion(request):
	if request.method == "POST":
		form = RegistroForm(request.POST)
		if form.is_valid():
			persona = form.save()
			return redirect('/')
	else:
		form = RegistroForm()
	return render(request, 'inicio/inscripcion.html', {'form' : form } )