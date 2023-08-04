from django.urls import path
from .views import *

urlpatterns = [
    path('product', ProductListAPIView.as_view())
]