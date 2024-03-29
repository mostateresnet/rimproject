from rest_framework import serializers
from rim.models import Equipment, EquipmentType
from .models import ApiError

class EquipmentSerializer(serializers.ModelSerializer):
    CPU = serializers.CharField(max_length=64, required=False, source='cpu')
    Displays = serializers.JSONField(required=False, source='displays')
    GPUs = serializers.JSONField(required=False, source='GPU')
    Hostname = serializers.CharField(max_length=100, required=False, source='hostname')
    Manufacturer = serializers.CharField(max_length=30, required=False, source='manufacturer')
    Model = serializers.CharField(max_length=30, source='equipment_model')
    NICs = serializers.JSONField(required=False, source='network_cards')
    RAM = serializers.CharField(max_length=255, required=False, source='memory')
    Serial = serializers.CharField(max_length=100, source='serial_no')
    Storage = serializers.JSONField(required=False, source='storage')
    Users = serializers.JSONField(required=False, source='users_info')
    EquipmentType = serializers.SlugRelatedField(queryset=EquipmentType.objects.all(), slug_field='type_name', required=False, allow_null=True, source='equipment_type')

    def validate_Serial(self, value):
        return value.upper()

    class Meta:
        model = Equipment
        fields = ('CPU', 'Displays', 'GPUs', 'Hostname', 'Manufacturer', 'Model', 'NICs', 'RAM', 'Serial', 'Storage', 'Users', 'EquipmentType')


class ApiErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiError
        fields = '__all__'
