# Create your views here.

from rest_framework.viewsets import ModelViewSet
from django.db.models import Prefetch
from .models import MultiSite
from .serializers import MultiSiteSerializer
from api.paginator import CustomPagination
# from silk.profiling.profiler import silk_profile
from sites.models import Site

class MultiSiteViewSet(ModelViewSet):
    queryset = MultiSite.objects.prefetch_related(
        Prefetch(lookup="sites",queryset=Site.objects.only("id", "company", "parent_company").select_related("company")))
    serializer_class = MultiSiteSerializer
    pagination_class = CustomPagination
    
    # @silk_profile(name='MultiSiteViewSet list')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)