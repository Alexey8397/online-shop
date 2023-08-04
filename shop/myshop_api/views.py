from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from myshop.models import Product
from .serializers import ProductSerializer
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


# class ProductAPIView(APIView):
#     def get(self, request, format=None):
#         return Response({"massage": "Hello world"})

class ProductListAPIView(generics.ListCreateAPIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListAPIViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class CustomAuthToken(ObtainAuthToken):
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#         })
