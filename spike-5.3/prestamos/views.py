from django.shortcuts import render
from .models import Prestamo


def lista(request):
    q = request.GET.get("q", "")

    prestamos = Prestamo.objects.select_related(
        "herramienta"
    )

    if q:
        prestamos = prestamos.filter(
            solicitante__icontains=q
        )

    return render(
        request,
        "lista.html",
        {
            "prestamos": prestamos,
            "q": q
        }
    )