from django.contrib import admin

# Register your models here.
from .models import ExpenseModel

admin.site.register(ExpenseModel)
