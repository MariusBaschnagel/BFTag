from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def datenschutz(request):
    return render(request, "datenschutz.html")


@login_required
def index(request):
    if request.method == "POST":
        data = request.POST
        print(data)
    return render(request, "index.html")
