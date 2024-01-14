from rest_framework.viewsets import ModelViewSet
from endereco.models import Endereco
from .serializers import EnderecoSerializer

class EnderecoViewSet(ModelViewSet):
    serializer_class = EnderecoSerializer

    def get_queryset(self):
        return Endereco.objects.all()