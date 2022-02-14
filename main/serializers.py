from rest_framework import serializers
from .models import Store, Visit, Employee


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name')


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('id', 'date', 'latitude', 'longitude', 'store')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'date': instance.date
        }

    def create(self, validated_data):
        request = self.context.get('request')
        phone = request.query_params.get('phone')
        employee = Employee.objects.filter(phone=phone).first()
        validated_data.update({'employee': employee})
        return Visit.objects.create(**validated_data)



