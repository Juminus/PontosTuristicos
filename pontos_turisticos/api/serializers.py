from rest_framework.serializers import ModelSerializer
from pontos_turisticos.models import PontosTurisicos

class PontosTurisicosSerializer(ModelSerializer):
    class Meta:
        model = PontosTurisicos
        fields = 'id', 'nome', 'descricao'