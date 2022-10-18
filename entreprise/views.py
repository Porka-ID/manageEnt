from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from entreprise.models import Entreprise

# Create your views here.
def index(request):
    return render(request, 'entreprise/index.html', context={})

def add_entreprise(request):
    name_ent = request.POST.get("ent-name")
    logo_ent = request.POST.get("ent-logo")
    num_ent = request.POST.get("ent-num")
    namepdg_ent = request.POST.get("ent-namepdg")
    Entreprise.objects.create(name=name_ent, logopath=logo_ent, numeroEnt=num_ent, namePDG=namepdg_ent)
    return HttpResponse("")