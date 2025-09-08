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


from rest_framework import serializers

class DailyNutrientSummarySerializer(serializers.Serializer):
    calories = serializers.FloatField()
    protein = serializers.FloatField()
    fat = serializers.FloatField()
    carbs = serializers.FloatField()
    vitamin_a = serializers.FloatField()
    vitamin_c = serializers.FloatField()
    
    calories_pct = serializers.FloatField()
    protein_pct = serializers.FloatField()
    fat_pct = serializers.FloatField()
    carbs_pct = serializers.FloatField()
    vitamin_a_pct = serializers.FloatField()
    vitamin_c_pct = serializers.FloatField()
