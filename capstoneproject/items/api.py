from items.models import Item
from rest_framework import viewsets, permissions
from .serializers import ItemSerializer

# Lead Viewset


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ItemSerializer
