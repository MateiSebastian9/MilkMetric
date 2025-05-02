from rest_framework import serializers
from .models import MilkMetric

class MilkMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkMetric
        fields = ['id', 'amount', 'temperature', 'humidity', 'timestamp']
        read_only_fields = ['timestamp']
