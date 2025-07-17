from django.shortcuts import render

# Create your views here.
from .serializer import ExpenseSerializer
from .models import ExpenseModel
from rest_framework import viewsets,permissions

class ExpenseViewsets(viewsets.ModelViewSet):
    queryset=ExpenseModel.objects.all()
    serializer_class=ExpenseSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    
    
    def get_queryset(self):
        return ExpenseModel.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)