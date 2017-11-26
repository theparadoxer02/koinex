from rest_framework import generics
from rest_framework import permissions
from . serializers import (
	BankDetailSerializer,
	KYCSerializer,
	KYC_DocumentSerializer,
	AccountSerializer,
)


class BankDetailCreateApiView(generics.CreateAPIView):
	serializer_class = BankDetailSerializer
	permission_classes = [permissions.IsAuthenticated]


class KYC_DocumentCreateApiView(generics.CreateAPIView):
	serializer_class = KYC_DocumentSerializer
	permission_classes = [permissions.IsAuthenticated]


class KYCCreateApiView(generics.CreateAPIView):
	serializer_class = KYCSerializer
	permission_classes = [permissions.IsAuthenticated]


class AccountCreateApiView(generics.CreateAPIView):
	serializer_class = AccountSerializer
	permission_classes = [permissions.IsAuthenticated]