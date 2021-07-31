from rest_framework.serializers import ModelSerializer
from protoapi.models import Record,Type,User

from drf_writable_nested.serializers import WritableNestedModelSerializer

# My Serializers
class TypeSerializer(WritableNestedModelSerializer,ModelSerializer):
    class Meta:
        model = Type
        depth = 4
        fields = '__all__'

class UserSerializer(WritableNestedModelSerializer,ModelSerializer):
    class Meta:
        model = User
        depth = 4
        fields = '__all__'
        
class RecordSerializer(WritableNestedModelSerializer,ModelSerializer):
    type_idtype = TypeSerializer(allow_null=True)#manual
    user_iduser = UserSerializer(allow_null=True)#manual
    class Meta:
        model = Record
        depth = 4
        fields = '__all__'