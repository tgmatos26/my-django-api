from django.contrib.auth.models import User, Group
from appDentista.models import Dentista, Produtos
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class DentistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dentista
        fields = ['url', 'name', 'cpf', 'cro', 'email', 'password', 'passwordConfirmation',
        'street', 'number', 'district', 'city', 'state']

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = ['url', 'name', 'lab', 'value']