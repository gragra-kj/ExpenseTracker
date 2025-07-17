from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ExpenseModel(models.Model):
    CATEGORY_CHOICES = [
        ("FOOD", "Food"),
        ("TRANSPORT", "Transport"),
        ("HEALTH", "Health"),
        ("ENTERTAINMENT", "Entertainment"),
        ("OTHER", "Other"),
    ]
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="expenses")
    title=models.CharField(max_length=120)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    category=models.CharField(max_length=100,choices=CATEGORY_CHOICES)
    date=models.DateField()
    notes=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.amount}"
    
