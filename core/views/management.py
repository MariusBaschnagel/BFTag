from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from core.models import Fahrzeug, Logmessage


def datenschutz(request):
    return render(request, "datenschutz.html")


@login_required
def index(request):
    if request.method == "POST":
        if "fahrzeuge" not in request.POST:
            messages.error(request, "Keine Fahrzeuge in Einsatz hinterlegt.")

        stichwort = request.POST["stichwort"]
        adresse = request.POST["adresse"]
        fstring = ""

        for f in request.POST.getlist("fahrzeuge"):
            fstring += Fahrzeug.objects.get(pk=f).shortname
            fstring += ", "
        fstring = fstring[:-2]

        log = Logmessage(stichwort=stichwort, adresse=adresse, fahrzeuge=fstring).save()
    return render(request, "index.html", context={
        "fahrzeuge": Fahrzeug.objects.all(),
        "logmessages": Logmessage.objects.filter(
            timestamp__gte=timezone.now() - timezone.timedelta(days=2)
        )
    })
