from rest_framework import serializers
from .models import FoodItem, FeedingRecord, Baby


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'


class FeedingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedingRecord
        fields = '__all__'


class DailySummarySerializer(serializers.Serializer):
    total_milk_ml = serializers.FloatField()
    total_calories = serializers.FloatField()
    total_protein = serializers.FloatField()
    breakdown = serializers.DictField()
