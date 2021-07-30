from rest_framework.viewsets import ModelViewSet
from protoapi.serializers import RecordSerializer, TypeSerializer, UserSerializer
from protoapi.models import Record,Type,User

from rest_framework.permissions import IsAuthenticated,SAFE_METHODS #MANUAL

class RecordViewSet(ModelViewSet):
    queryset = Record.objects.order_by('pk')
    serializer_class = RecordSerializer
    filter_fields = '__all__'
    # permission_classes = (IsAuthenticated,)


class TypeViewSet(ModelViewSet):
    queryset = Type.objects.order_by('pk')
    serializer_class = TypeSerializer
    filter_fields = '__all__'
    # permission_classes = (IsAuthenticated,)


class UserViewSet(ModelViewSet):
    queryset = User.objects.order_by('pk')
    serializer_class = UserSerializer
    filter_fields = '__all__'
    # permission_classes = (IsAuthenticated,)
