from rest_framework import serializers
from .models import Herramienta, Prestamo


class HerramientaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Herramienta
        fields = ["id", "nombre", "descripcion", "fecha_creacion"]


class PrestamoNestedSerializer(serializers.ModelSerializer):
    herramienta = HerramientaSerializer()

    class Meta:
        model = Prestamo
        fields = [
            "id",
            "solicitante_nombre",
            "solicitante_apellido",
            "herramienta",
            "fecha_prestamo",
            "fecha_devolucion",
            "estado",
        ]


class PrestamoFlatSerializer(serializers.ModelSerializer):
    herramienta_id = serializers.IntegerField(source="herramienta.id", read_only=True)
    herramienta_nombre = serializers.CharField(source="herramienta.nombre", read_only=True)

    class Meta:
        model = Prestamo
        fields = [
            "id",
            "solicitante_nombre",
            "solicitante_apellido",
            "herramienta_id",
            "herramienta_nombre",
            "fecha_prestamo",
            "fecha_devolucion",
            "estado",
        ]