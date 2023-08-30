# Create your views here.

from rest_framework.viewsets import ModelViewSet
from django.db.models import Prefetch
from .models import MultiSite
from .serializers import MultiSiteSerializer
from api.paginator import CustomPagination
# from silk.profiling.profiler import silk_profile
from sites.models import Site
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
class MultiSiteViewSet(ModelViewSet):
    queryset = MultiSite.objects.prefetch_related(
        Prefetch(lookup="sites",queryset=Site.objects.only("id", "company").select_related("company")))
    serializer_class = MultiSiteSerializer
    pagination_class = CustomPagination
    
    # @silk_profile(name='MultiSiteViewSet list')
    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        
        if request.query_params.get("brief", None):
            serializer = self.get_serializer(qs, many=True)
            return Response(serializer.data)
        
        return super().list(request, *args, **kwargs)
        
        
class multisite(ListAPIView):
    queryset = MultiSite.objects.all()
    serializer_class = MultiSiteSerializer
    pagination_class = None
    
    