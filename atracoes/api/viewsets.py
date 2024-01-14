from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer


class AtracaoViewSet(ModelViewSet):
    serializer_class = AtracaoSerializer

    def get_queryset(self):
        return Atracao.objects.all()