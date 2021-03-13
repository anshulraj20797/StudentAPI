from rest_framework import serializers
from .models import Address,Student
from rest_framework.views import Response,status

class AddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    city = serializers.CharField(max_length=100)
    landmark = serializers.CharField(max_length=100)
    postal_address = serializers.CharField(max_length=250)


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    student_name = serializers.CharField(max_length=100)
    standard = serializers.IntegerField(min_value=0)
    address = AddressSerializer(read_only=False)


    def create(self, validated_data):
        address = AddressSerializer(read_only=False, many=True)
        address_1 = validated_data.pop('address')
        address_2 = Address.objects.create(**address_1) 
        validated_data['address_id']=address_2.id
        s1 = Student.objects.create(**validated_data)
        return s1

    