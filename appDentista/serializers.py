from django.contrib.auth.models import User, Group
from appDentista.models import Dentists, Drivers, Labs, Products, Orders, Transports
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class DentistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dentists
        fields = ['url', 'name', 'cpf', 'cro', 'email', 'phone','password',
        'street', 'number', 'district', 'city', 'state']

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields = ['url', 'name', 'cpf', 'cnh', 'crlv', 'email', 'phone','password',
        'street', 'number', 'district', 'city', 'state']

class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labs
        fields = ['url', 'name', 'cnpj', 'insc_cfo', 'email', 'phone','password',
        'street', 'number', 'district', 'city', 'state']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['url', 'id', 'name', 'lab', 'description', 'value', 'production']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['url', 'id', 'id_product', 'dentist']

class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transports
        fields = ['url', 'id', 'id_order', 'cpf_driver','value', 'estimated_time']