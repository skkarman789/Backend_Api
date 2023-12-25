from rest_framework import serializers
from .models import AlertThreshold, Data, Alert

class AlertThresholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertThreshold
        fields = '__all__'

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'