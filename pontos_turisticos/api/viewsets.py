from rest_framework.viewsets import ModelViewSet
from pontos_turisticos.models import PontosTurisicos
from .serializers import PontosTurisicosSerializer


class PontosTuristicosViewSet(ModelViewSet):
    queryset = PontosTurisicos.objects.all()
    serializer_class = PontosTurisicosSerializer