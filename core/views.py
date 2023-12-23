# views.py
from rest_framework import viewsets, filters


from core.pagination import MyPagination
from .models import YourModel
from .serializers import YourModelSerializer
from django_filters.rest_framework import DjangoFilterBackend

# from rest_framework.decorators import action
# from rest_framework.response import Response


class YourModelViewSet(viewsets.ModelViewSet):
    queryset = YourModel.objects.all().order_by('id')
    serializer_class = YourModelSerializer
    pagination_class = MyPagination  
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields =  ['id','description', 'name']  # Specify fields to filter
    ordering_fields = '__all__'  


     # ---------------------------------------------------------------------------- #
     #                @  USE IF YOU WANT TO CUSTOMIZE ANY FUNCTION                  #
     # ---------------------------------------------------------------------------- #
    # /api/your-model/{pk}/custom_function/
    # def get_queryset(self):
    #     # Custom logic to filter or modify the queryset
    #     queryset = YourModel.objects.all()
    #     # Example: Only include objects created by the authenticated user
    #     if self.request.user.is_authenticated:
    #         queryset = queryset.filter(created_by=self.request.user)
    #     return queryset


    # ---------------------------------------------------------------------------- #
    #           @  USE IF YOU WANT TO ADD ANY CUSTOM NEW FUNCTION                  #
    # ---------------------------------------------------------------------------- #

    # from rest_framework.decorators import action
    # from rest_framework.response import Response
    # @action(detail=True, methods=['get'])
    # def custom_function(self, request, pk=None):
    #     instance = self.get_object()
    #     serializer = YourModelSerializer(instance)
    #     # Your custom logic using the serializer function
    #     # For example, you can modify the serializer data or perform additional actions
    #     modified_data = {'modified_field': serializer.data['some_field']}
    #     return Response(modified_data)


