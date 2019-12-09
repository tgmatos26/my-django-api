from django.contrib.auth.models import User, Group
from appDentista.models import Dentista, Produtos
from rest_framework import viewsets
from appDentista.serializers import UserSerializer, GroupSerializer, DentistaSerializer, ProdutosSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class DentistaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Dentista.objects.all()
    serializer_class = DentistaSerializer

class ProdutosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer