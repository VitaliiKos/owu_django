from rest_framework.serializers import ModelSerializer

from apps.computers.models import ComputerModel


class ComputerSerializer(ModelSerializer):
    class Meta:
        model = ComputerModel
        fields = ('id', 'brand', 'computer_model', 'memory_capacity', 'monitor')
