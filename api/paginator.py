from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 5
    page_query_param='p'
    page_size_query_param = 'records'
    

class MultiplePaginationMixin:
    def get_pagination_class(self):
        return self.pagination_class

    @property
    def paginator(self):
        pagination_class = self.get_pagination_class()
        if pagination_class is None:
            return None
        return pagination_class()
    