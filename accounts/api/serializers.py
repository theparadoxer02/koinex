from rest_framework import serializers
from accounts.models import Account, KYC, KYC_Document, BankDetail

class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = [
			'status_option',
			'user',
			'first_name',
			'last_name',
			'email',
			'asknbid_id',
			'account_status',
			'accont_created_on',
		]


class KYCSerializer(serializers.ModelSerializer):
	class Meta:
		model = KYC
		fields = [
				'kyc_status',
				'Account',
				'dob',
				'full_name',
				'pan_number',
				'adhaar_no',
				'gross_annual_income',
				'residential_status',
				'street_address',
				'city',
				'state',
				'country',
				'pin_code',
				'kyc_status',
				'valid'
			]

class KYC_DocumentSerializer(serializers.ModelSerializer):
	class Meta:
		model = KYC_Document
		fields = [
			'Account',
			'pan_card',
			'adhaar_card',
			'adhaar_back',
			'photograph',
			'valid',
		]


class BankDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = BankDetail
		fields = [
			'Account',
			'ifsc_code',
			'time',
			'source',
			'ip',
			'activity',
			'status',
			'valid'
		]