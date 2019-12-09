from django.contrib.auth.models import User, Group
from appDentista.models import Dentists, Drivers, Labs, Products, Orders, Transports
from rest_framework import viewsets
from appDentista.serializers import UserSerializer, GroupSerializer
from appDentista.serializers import DentistSerializer, DriverSerializer, LabSerializer
from appDentista.serializers import ProductSerializer, OrderSerializer, TransportSerializer

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

class DentistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Dentists.objects.all()
    serializer_class = DentistSerializer

class DriverViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Drivers.objects.all()
    serializer_class = DriverSerializer

class LabViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Labs.objects.all()
    serializer_class = LabSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    
class TransportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Transports.objects.all()
    serializer_class = TransportSerializer