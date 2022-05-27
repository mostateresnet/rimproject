from rest_framework import mixins, generics, status
from rest_framework.response import Response

from rim.models import Equipment, EquipmentType
from .models import ApiError
from .serializers import EquipmentSerializer, ApiErrorSerializer
from .helpers import validate_req_hash, get_client_ip

class EquipmentCreateOrUpdate(mixins.CreateModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    lookup_field = 'serial_no'

    def post(self, request, *args, **kwargs):
        if validate_req_hash(request.data, 'code'):
            serializer = EquipmentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            if not Equipment.objects.filter(serial_no=serializer.data['Serial']).exists():
                return self.create(request, *args, **kwargs)
            else:
                self.kwargs['serial_no'] = serializer.data['Serial']
                return self.update(request, *args, **kwargs)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class AddApiError(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = ApiError.objects.all()
    serializer_class = ApiErrorSerializer

    def post(self, request, *args, **kwargs):
        if validate_req_hash(request.data, 'code'):
            request.data['error_type'] = "API Invoker Failed"
            request.data['ip_address'] = get_client_ip(request)
            return self.create(request, *args, **kwargs)
        return Response(status=status.HTTP_400_BAD_REQUEST)


