from rest_framework import  pagination
from rest_framework.response import Response
from rest_framework.exceptions import NotFound



class MyPaginationWithAllDetails(pagination.PageNumberPagination):
    page_size = 14  
    page_size_query_param = 'page_size'
    max_page_size = 100


class MyPagination(pagination.PageNumberPagination):
    page_size = 14  
    page_size_query_param = 'page_size'
    max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        try:
            return super().paginate_queryset(queryset, request, view)
        except NotFound:
            return [] # return empty list instead of not found json
    

    # get only results list 
    def get_paginated_response(self, data):
        return Response(data)