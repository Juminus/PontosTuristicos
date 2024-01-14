from rest_framework.viewsets import ModelViewSet
from pontos_turisticos.models import PontoTurisico
from .serializers import PontosTurisicosSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontosTurisicosSerializer

    def get_queryset(self):
        return PontoTurisico.objects.filter(aprovado=True)