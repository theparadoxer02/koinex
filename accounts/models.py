from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
	" Accounts "
	status_option = (
		('Submitted', 'Submitted'),
		('Verified', 'Verified',),
		('Rejected', 'Rejected'),
	)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=40, default='', null=False)
	last_name = models.CharField(max_length=40, default='', null=False)
	email = models.EmailField(null=False, max_length=254)
	asknbid_id = models.CharField(max_length=30, unique=True, null=True)
	account_status = models.CharField(max_length=20, choices=status_option)
	accont_created_on = models.DateField(auto_now=True, auto_now_add=False)

class KYC(models.Model):
	kyc_status = (
		('Submitted', 'Submitted'),
		('Pending','Pending'),
		('Verified','Verified'),
	)
	Account = models.ForeignKey(Account, on_delete=models.CASCADE)
	dob = models.DateField(auto_now=False, auto_now_add=False)
	full_name = models.CharField(max_length=100, null=False)
	pan_number = models.CharField(max_length=10, default='')
	adhaar_no = models.CharField(max_length=12, default='')
	gross_annual_income = models.CharField(max_length=12, default='')
	residential_status = models.CharField(max_length=200, default='')
	street_address = models.CharField(max_length=30, default='')
	city = models.CharField(max_length=30, default='')
	state = models.CharField(max_length=30, default='')
	country = models.CharField(max_length=30, default='')
	pin_code = models.CharField(max_length=10, default='')
	kyc_status = models.CharField(max_length=30, choices=kyc_status)
	valid = models.BooleanField(default=False)


class KYC_Documents(models.Model):
	Account = models.ForeignKey(Account, on_delete=models.CASCADE)
	pan_card = models.ImageField(upload_to='media/upload/pancard')
	adhaar_card = models.ImageField(upload_to='media/upload/adhaarcard')
	adhaar_back = models.ImageField(upload_to='media/upload/adhaarback')
	photograph = models.ImageField(upload_to='media/upload/photograph')
	valid = models.BooleanField(default=False)


class BankDetail(models.Model):
	Account = models.ForeignKey(Account, on_delete=models.CASCADE)
	ifsc_code = models.CharField(max_length=10, default='', null=False)
	time = models.TimeField(auto_now=False, auto_now_add=True)
	# Not sure about it
	source = models.CharField(max_length=100, default='')
	ip = models.GenericIPAddressField()
	activity = models.TextField()
	status = models.BooleanField(default=False)
	valid = models.BooleanField(default=False)
