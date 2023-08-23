# Create your views here.

from rest_framework.viewsets import ModelViewSet

from .models import MultiSite
from .serializers import MultiSiteSerializer
from api.paginator import CustomPagination


class MultiSiteViewSet(ModelViewSet):
    queryset = MultiSite.objects.all()
    serializer_class = MultiSiteSerializer
    pagination_class = CustomPagination
