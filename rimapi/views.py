from hashlib import sha256
from django.conf import settings
from rest_framework import mixins, generics, status
from rest_framework.response import Response

from rim.models import Equipment
from .models import ApiError
from .serializers import EquipmentSerializer, ApiErrorSerializer

API_SECRET = getattr(settings, "API_SECRET", 'test_secret_key')

class EquipmentCreateOrUpdate(mixins.CreateModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    lookup_field = 'serial_no'

    def post(self, request, *args, **kwargs):
        if validate_req_hash(request.data, 'Serial'):
            return self.create(request, *args, **kwargs)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        if validate_req_hash(request.data, 'Serial'):
            self.kwargs['serial_no'] = request.data['Serial']
            return self.update(request, *args, **kwargs)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class AddApiError(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = ApiError.objects.all()
    serializer_class = ApiErrorSerializer

    def post(self, request, *args, **kwargs):
        if validate_req_hash(request.data, 'code'):
            request.data['error_type'] = "API Invoker Failed"
            return self.create(request, *args, **kwargs)
        return Response(status=status.HTTP_400_BAD_REQUEST)


def validate_req_hash(data, key):
    if "hash" in data and data['hash'].lower() == sha256((str(data[key]) + API_SECRET).encode('utf-8')).hexdigest():
        del data['hash']
        return True
    return False