from django.contrib.auth.models import User, Group
from django.shortcuts import render
from vtormet.models import Requisition, RequisitionItem, RequisitionBid, Customer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication


from django.conf import settings 
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager, PermissionsMixin
)



class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	permission_classes = [permissions.IsAuthenticated]

#Возвращаем все ценные предметы в конкретной заявке
class RequisitionItemsViewSet(APIView):
	serializer_class = RequisitionItemsSerializer


	def get_queryset(self): 
		req_items = RequisitionItem.objects.all()
		return req_items

	def get(self, request, *args, **kwargs):

		try:
			id = request.query_params["id"]
			if id != None:
				req_item = RequisitionItem.objects.get(id=id)
				serializer = RequisitionItemsSerializer(req_item)
		except:
				req_items = self.get_queryset()
				serializer = RequisitionItemsSerializer(req_items, many=True)

		return Response(serializer.data)

#Возвращаем JSON со всемизаявками||заявками конкретного пользователя
class RequisitionsViewSet(APIView):
	authentication_classes = [JWTAuthentication]
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = RequisitionsSerializer

	def get_queryset(self):
		requisitions = Requisition.objects.all()
		return requisitions

	def get(self, request, *args, **kwargs):
		if ('id' in request.query_params):
			requisition = Requisition.objects.get(id=request.query_params['id'])
			serializer = RequisitionsSerializer(requisition)
		else:
			if ('customer_id' in request.query_params):
				if ('exclude_user' in request.query_params):
					customer = Customer.objects.get(user=request.query_params['customer_id'])
					requisitions = Requisition.objects.exclude(customer=customer)
				else:
					requisitions = Requisition.objects.filter(customer=request.query_params['customer_id'])

			else:
				requisitions = self.get_queryset()
			serializer = RequisitionsSerializer(requisitions, many=True) 

		return Response(serializer.data)


#Возвращаем JSON со ставками по заявке||пользователю||вообще все ставки
class BidsViewSet(APIView):
	authentication_classes = [JWTAuthentication]
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = BidsSerializer

	def get_queryset(self):
		bids = RequisitionBid.objects.all()
		return bids

	def get(self, request, *args, **kwargs):
		if ('id' in request.query_params):
			bid = RequisitionBid.objects.get(id=request.query_params['id'])
			serializer = BidsSerializer(bid)
		else:
			if ('requisition' in request.query_params):
				bids = RequisitionBid.objects.filter(requisition=request.query_params['requisition'])
			elif ('customer'  in request.query_params):
				bids = RequisitionBid.objects.filter(customer=request.query_params['customer'])
			else:
				bids = self.get_queryset()
			serializer = BidsSerializer(bids, many=True) 
		return Response(serializer.data)

	def post(self, request, *args, **kwargs):
		bid_data = request.data
		bid_sum = bid_data["bid_sum"]
		customer = Customer.objects.get(id=bid_data["customer"])
		requisition = Requisition.objects.get(id=bid_data["requisition"])
		bid = RequisitionBid.objects.create(
			bid_sum = bid_sum,
			customer = customer,
			requisition = requisition,
		)
		bid.save()
		bid.place_a_bet()
		serializer = BidsSerializer(bid)

		return Response(serializer.data)



