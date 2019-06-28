from rest_framework import viewsets

from ghostpostbackend.models import BoastRoastModel
from ghostpostbackend.serializers import BoastRoastSerializer


# should get full stuff; modelviewset; some lbuiltin stuff; form create/create function
class BoastRoastViewSet(viewsets.ModelViewSet):
    queryset = BoastRoastModel.objects.all()
    serializer_class = BoastRoastSerializer
    
    # def create(self, request, *args, **kwargs):
    #     BoastRoastModel.objects.create(request.data)