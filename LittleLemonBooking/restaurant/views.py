from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.shortcuts import render
from .models import Menu, Booking 
from .serializers import MenuSerializer, BookingSerializer


# Create your views here. 
def index(request):
    return render(request, 'index.html',{})

class MenuItemsView(generics.ListCreateAPIView):

    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAdminUser] 
        return[permission() for permission in permission_classes]

    queryset = Menu.objects.all().order_by('-id')
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):

    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAdminUser] 
        return[permission() for permission in permission_classes]

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer