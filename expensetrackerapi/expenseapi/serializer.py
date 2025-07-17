from .models import ExpenseModel
from rest_framework import serializers

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=ExpenseModel
        fields="__all__"
        read_only_fields = ["user", "created_at"]

        
        