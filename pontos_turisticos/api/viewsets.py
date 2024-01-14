from rest_framework.viewsets import ModelViewSet
from pontos_turisticos.models import PontoTurisico
from .serializers import PontosTurisicosSerializer


class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTurisico.objects.all()
    serializer_class = PontosTurisicosSerializer