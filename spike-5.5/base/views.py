from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Prestamo
from .serializer import PrestamoNestedSerializer, PrestamoFlatSerializer
from rest_framework.pagination import PageNumberPagination


class PrestamoPagination(PageNumberPagination):
    page_size = 20


class PrestamoNestedView(generics.ListAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoNestedSerializer


class PrestamoNestedOptimizedView(generics.ListAPIView):
    serializer_class = PrestamoNestedSerializer

    def get_queryset(self):
        return Prestamo.objects.select_related("herramienta").all()


class PrestamoFlatView(generics.ListAPIView):
    queryset = Prestamo.objects.select_related("herramienta").all()
    serializer_class = PrestamoFlatSerializer


class PrestamoNestedPaginatedView(generics.ListAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoNestedSerializer
    pagination_class = PrestamoPagination


class PrestamoNestedOptimizedPaginatedView(generics.ListAPIView):
    serializer_class = PrestamoNestedSerializer
    pagination_class = PrestamoPagination

    def get_queryset(self):
        return Prestamo.objects.select_related("herramienta").all()


class PrestamoFlatPaginatedView(generics.ListAPIView):
    queryset = Prestamo.objects.select_related("herramienta").all()
    serializer_class = PrestamoFlatSerializer
    pagination_class = PrestamoPagination