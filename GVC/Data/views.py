from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from Data import serializers, models

# Create your views here.


class TiVAViewSet(ModelViewSet):
    serializer_class = serializers.TradeInValueAddedSerializer
    queryset = models.TradeInValueAdded.objects.all()
    permission_classes = [permissions.AllowAny]

    @action(
        methods=['get', 'post', 'patch', 'delete'],
        detail=True,
        serializer_class=serializers.TradeInValueAddedSerializer,
        url_path='TiVA_analytics'
    )
    def analysis(self, request, *args, **kwargs):
        """
        This method is used to perform analysis on TradeInValueAdded model as well as 
        Year model and ImportDatabase model.
        """
        if request.method == 'GET':
            pass
        if request.method == 'POST':
            pass
        if request.method == 'PATCH':
            pass
        if request.method == 'DELETE':
            pass

        # return self.response(request, *args, **kwargs)
