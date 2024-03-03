from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .. import models


def datenschutz(request):
    return render(request, "datenschutz.html")


@login_required
def index(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        if "fahrzeug" not in data:
            messages.error(request, "Keine Fahrzeuge in Einsatz hinterlegt.")
    return render(request, "index.html", context={"fahrzeuge": models.Fahrzeug.objects.all()})
