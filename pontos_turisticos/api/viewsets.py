from rest_framework.viewsets import ModelViewSet
from pontos_turisticos.models import PontoTurisico
from .serializers import PontosTurisicosSerializer
from rest_framework.decorators import action



class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontosTurisicosSerializer

    def get_queryset(self):
        return PontoTurisico.objects.filter(aprovado=True)
    
    @action(methods=['post', 'get'], detail=True)
    def denunciar(self, request, pk=None):
        pass