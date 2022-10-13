from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Cvetmet(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	image = models.ImageField(upload_to='cvetmet/%Y/%m/%d', blank=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)


class Raddet_category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	image = models.ImageField(upload_to='raddet/%Y/%m/%d', blank=True)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name


class Raddet(models.Model):
	image = models.ImageField(upload_to='raddet/%Y/%m/%d', blank=True)
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	retail = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	opt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	category = models.ForeignKey(Raddet_category, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Customer(models.Model):	
	name = models.CharField(max_length=200, db_index=True)
	organization = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, unique=True)
	image = models.ImageField(upload_to='customer/%Y/%m/%d', blank=True)
	email = models.EmailField(max_length=200, db_index=True)
	phone = models.CharField(max_length=200, db_index=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.organization


class Letter(models.Model):
	phone = models.CharField(max_length=200, db_index=True)
	category = models.IntegerField()


class Recycling(models.Model):
	FkkoCode = models.CharField(max_length=20, db_index=True, primary_key=True, default=None)
	FkkoDescription = models.TextField(max_length=300, blank=True)
	collection = models.BooleanField(default=False)
	transportation = models.BooleanField(default=False)
	processing = models.BooleanField(default=False)
	disposal = models.BooleanField(default=False)
	utilization = models.BooleanField(default=False)
	placement = models.BooleanField(default=False)


class RequisitionItem(models.Model):
	os_number = models.CharField(max_length=50, db_index=True)
	serial_number = models.CharField(max_length=50, db_index=True)
	sap_material = models.CharField(max_length=50, db_index=True)
	name = models.CharField(max_length=50, db_index=True)
	quantity = models.IntegerField()
	comment = models.CharField(max_length=100, db_index=True)

	def __str__(self):
		return self.sap_material


class Requisition(models.Model):
	number_in = models.CharField(max_length=50, db_index=True, default=None)
	number_out = models.CharField(max_length=50, db_index=True, default=None)
	registration_date = models.DateTimeField(auto_now_add=True)
	start_date = models.DateTimeField(default=None)
	end_date = models.DateTimeField(default=None)
	requisition_item = models.ManyToManyField(RequisitionItem, default=None)
	customer = models.ForeignKey(Customer, default=None, on_delete=models.SET_DEFAULT)
	bid_sum = models.FloatField()
	city = models.CharField(max_length=50, db_index=True, default=None)
	status = models.IntegerField(default=0)

	def __str__(self):
		return '%s/%s'%(self.number_in, self.number_out)


class RequisitionBid(models.Model):
	customer = models.ForeignKey(Customer,  on_delete=models.CASCADE)
	requisition = models.ForeignKey(Requisition,  on_delete=models.CASCADE)
	bid_sum = models.FloatField()

	def place_a_bet(self, *args, **kwargs):
		requisition = Requisition.objects.get(id = self.requisition.id)
		max_bid = RequisitionBid.objects.filter(requisition = self.requisition.id).aggregate(models.Max('bid_sum'))
		if (float(self.bid_sum) > float(requisition.bid_sum)):
			requisition.bid_sum  = float(self.bid_sum)
			requisition.customer = self.customer
			requisition.save()
		else:
			raise Exception('The new value must be greater than the previous one (%s)'%requisition.bid_sum)

