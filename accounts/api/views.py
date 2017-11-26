from rest_framework import generics
from rest_framework import permissions
from . serializers import (
	BankDetailSerializer,
	KYCSerializer,
	KYC_DocumentSerializer,
	AccountSerializer,
)


class BankDetailCreateAPiView(generics.CreateAPIView):
	serializer_class = BankDetailSerializer
	permission_classes = [permissions.IsAuthenticated]


class KYC_DocumentCreateAPiView(generics.CreateAPIView):
	serializer_class = KYC_DocumentSerializer
	permission_classes = [permissions.IsAuthenticated]


class KYCCreateAPiView(generics.CreateAPIView):
	serializer_class = KYCSerializer
	permission_classes = [permissions.IsAuthenticated]


class AccountCreateAPiView(generics.CreateAPIView):
	serializer_class = AccountSerializer
	permission_classes = [permissions.IsAuthenticated]