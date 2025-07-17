from rest_framework.routers import DefaultRouter
from .views import ExpenseViewsets
from django.urls import path,include

router=DefaultRouter()
router.register(r'expenses',ExpenseViewsets,basename='expense')

urlpatterns=[
    path('',include(router.urls))
]