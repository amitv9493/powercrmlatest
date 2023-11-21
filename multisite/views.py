# Create your views here.

from django.db.models import Prefetch
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from api.paginator import CustomPagination

# from silk.profiling.profiler import silk_profile
from sites.models import Site

from .models import MultiSite
from .serializers import MultiSiteSerializer


class MultiSiteViewSet(ModelViewSet):
    queryset = MultiSite.objects.prefetch_related(
        Prefetch(
            lookup="sites",
            queryset=Site.objects.only("id", "company").select_related("company"),
        )
    )
    serializer_class = MultiSiteSerializer
    pagination_class = CustomPagination

    @property
    def paginator(self):
        if self.request.query_params.get("brief", None):
            return None
        return super().paginator

    # def get_queryset(self):
    #     if self.request.query_params.get("brief", None):
    #         self.serializer_class.Meta.fields = ["id", "group_name", "group_type"]

    #     return super().get_queryset()

    def get_serializer(self, *args, **kwargs):
        if self.request.query_params.get("brief", None):
            kwargs["fields"] = ["id", "group_name"]
        return super().get_serializer(*args, **kwargs)

    # @silk_profile(name='MultiSiteViewSet list')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class multisite(ListAPIView):
    queryset = MultiSite.objects.all()
    serializer_class = MultiSiteSerializer
    pagination_class = None
    serializer_class = MultiSiteSerializer
    pagination_class = None
