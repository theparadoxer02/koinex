from django.conf.urls import url

from accounts.api.views import (
	BankDetailCreateApiView,
	KYCCreateApiView,
	KYC_DocumentCreateApiView,
	AccountCreateApiView
	)

urlpatterns = [
	url(r'^accounts/$', AccountCreateApiView.as_view(), name='accounts'),
	url(r'^bank/$', BankDetailCreateApiView.as_view(), name='bankdetail'),
	url(r'^kyc/$', KYCCreateApiView.as_view(), name='kyc'),
	url(r'^kycdocument/$', KYC_DocumentCreateApiView.as_view(), name='kycdocument'),

]