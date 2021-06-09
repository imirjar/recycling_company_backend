from django.db import models
from django.urls import reverse


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

	class Meta:
		ordering = ('name',)
		verbose_name = 'raddet_category'
		verbose_name_plural = 'raddet_categories'

	def get_absolute_url(self):
	        return reverse('vtormet:raddets', args=[self.slug])


	def __str__(self):
		return self.name


class Raddet(models.Model):
	image = models.ImageField(upload_to='raddet/%Y/%m/%d', blank=True)
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	retail = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	opt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	category = models.ForeignKey(Raddet_category, on_delete=models.CASCADE)


class Customer(models.Model):	
	name = models.CharField(max_length=200, db_index=True)
	organization = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, unique=True)
	image = models.ImageField(upload_to='customer/%Y/%m/%d', blank=True)
	email = models.EmailField(max_length=200, db_index=True)
	phone = models.CharField(max_length=200, db_index=True)


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

	#FkkoCode;FkkoDescription;collection;transportation;processing;disposal;utilization;placement
	

