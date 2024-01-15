from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField


from pontos_turisticos.models import PontoTurisico
from atracoes.api.serializers import AtracaoSerializer
from endereco.api.serializers import EnderecoSerializer

class PontosTurisicosSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()

    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTurisico
        fields = 'id', 'nome', 'descricao', 'foto', 'atracoes', 'comentarios', 'avaliacoes', 'endereco', 'descricao_completa', 


    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
