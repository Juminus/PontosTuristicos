from rest_framework.serializers import ModelSerializer
from pontos_turisticos.models import PontoTurisico

class PontosTurisicosSerializer(ModelSerializer):
    class Meta:
        model = PontoTurisico
        fields = 'id', 'nome', 'descricao'