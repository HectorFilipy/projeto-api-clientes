from rest_framework import serializers
from clientes.models import Cliente
from clientes.validatos import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"Número de CPF inválido"})
    
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O RG deve conter 9 dígitos."})
        
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Não inclua números neste campo."})
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O Número de celular deve seguir este exemplo: 84 91234-1234."})

        return data
