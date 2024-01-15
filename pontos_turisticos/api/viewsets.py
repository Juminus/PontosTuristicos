from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication

from pontos_turisticos.models import PontoTurisico
from .serializers import PontosTurisicosSerializer



class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontosTurisicosSerializer
    permission_classes = (DjangoModelPermissions, )
    authentication_classes = (TokenAuthentication, )
    #filter_backends = [SearchFilter, ] Não funciona!
    filterset_fields = ('id', 'nome', 'descricao')
    


    def get_queryset(self):
        return PontoTurisico.objects.all()

    @action(methods=['post', 'get'], detail=True)
    def denunciar(self, request, pk=None):
        pass