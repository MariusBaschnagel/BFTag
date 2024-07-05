from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from core.models import Vehicle, Operation


def datenschutz(request):
    return render(request, "datenschutz.html")


@login_required
def index(request):
    if request.method == "POST":
        if "fahrzeuge" not in request.POST:
            messages.error(request, _("No vehicles selected."))

        keyword = request.POST["stichwort"]
        address = request.POST["adresse"]
        fstring = ""

        for f in request.POST.getlist("fahrzeuge"):
            fstring += Vehicle.objects.get(pk=f).shortname
            fstring += ", "
        fstring = fstring[:-2]

        op = Operation(keyword=keyword, address=address, vehicles=fstring).save()
    return render(
        request,
        "index.html",
        context={
            "vehicles": Vehicle.objects.all(),
            "operations": Operation.objects.filter(
                dispatched__gte=timezone.now() - timezone.timedelta(days=2)
            ),
        },
    )


def operation_details(request, id: int):
    return render(request, "operation_details.html")
