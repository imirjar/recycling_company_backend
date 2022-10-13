from django.contrib.auth.models import User, Group
from vtormet.models import Requisition, RequisitionItem, RequisitionBid
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'name']


class RequisitionItemsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RequisitionItem
        fields = [
            'id',
            'os_number',
            'serial_number',
            'sap_material',
            'name',
            'quantity',
            'comment',
        ]




class RequisitionsSerializer(serializers.ModelSerializer):

    requisition_item = RequisitionItemsSerializer(read_only=True, many=True)

    class Meta:
        model = Requisition
        fields = [
            'id',
            'number_in',
            'number_out',
            'registration_date',
            'start_date',
            'end_date',
            'requisition_item', 
            'city',
            'customer',
            'bid_sum',
            'status',
        ]


class BidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequisitionBid
        fields = [
            'id',
            'customer',
            'requisition',
            'bid_sum',
        ]

