from rest_framework.serializers import ModelSerializer

from .models import Dni, Cele

class DniSerializer(ModelSerializer): 
    class Meta:
        model = Dni
        fields = ['id', 'title', 'detail']

class CeleSerializer(ModelSerializer):
    class Meta:
        model = Cele
        fields = ['id','cele', 'check', 'dni']




