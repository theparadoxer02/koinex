from django.contrib import admin
from .models import Account, KYC, KYC_Document, BankDetail

admin.site.register(Account)
admin.site.register(KYC)
admin.site.register(KYC_Document)
admin.site.register(BankDetail)