from rest_framework.viewsets import ModelViewSet
from .models import Dni, Cele
from .serializer import DniSerializer, CeleSerializer


class DniViewSet(ModelViewSet): 
    queryset = Dni.objects.all()
    serializer_class = DniSerializer 



class CeleViewSet(ModelViewSet): 
    queryset = Cele.objects.all()
    serializer_class = CeleSerializer

