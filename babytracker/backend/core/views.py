from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import datetime
from .models import FoodItem, FeedingRecord, Baby
from .serializers import FoodItemSerializer, FeedingRecordSerializer, DailySummarySerializer


class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, is_custom=True)


class FeedingRecordViewSet(viewsets.ModelViewSet):
    queryset = FeedingRecord.objects.all()
    serializer_class = FeedingRecordSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def baby_daily_summary(request, baby_id):
    date_str = request.GET.get('date')
    date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()

    records = FeedingRecord.objects.filter(
        baby_id=baby_id,
        fed_at__date=date_obj
    )

    total_milk_ml = 0
    total_calories = 0
    total_protein = 0
    breakdown = {}

    for record in records:
        total_milk_ml += record.amount_ml if record.food_item.name.lower() == 'milk' else 0
        total_calories += record.calories
        total_protein += record.protein
        food_name = record.food_item.name
        if food_name not in breakdown:
            breakdown[food_name] = {'amount_ml': 0, 'calories': 0}
        breakdown[food_name]['amount_ml'] += record.amount_ml
        breakdown[food_name]['calories'] += record.calories

    data = {
        'total_milk_ml': total_milk_ml,
        'total_calories': total_calories,
        'total_protein': total_protein,
        'breakdown': breakdown
    }

    serializer = DailySummarySerializer(data)
    return Response(serializer.data)




from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from django.utils.timezone import make_aware
from .models import Baby, FeedingRecord, NutrientGoal
from .serializers import DailyNutrientSummarySerializer

class DailySummaryWithGoalsAPIView(APIView):
    def get(self, request, baby_id):
        date_str = request.query_params.get('date')
        if not date_str:
            return Response({"error": "Date param required, format YYYY-MM-DD"}, status=400)
        
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        start_dt = make_aware(datetime.combine(date, datetime.min.time()))
        end_dt = make_aware(datetime.combine(date, datetime.max.time()))
        
        baby = Baby.objects.get(id=baby_id)
        feedings = FeedingRecord.objects.filter(baby=baby, fed_at__range=(start_dt, end_dt))
        
        total_calories = sum(f.calories for f in feedings)
        total_protein = sum(f.protein for f in feedings)
        total_fat = sum(f.fat for f in feedings)
        total_carbs = sum(f.carbs for f in feedings)
        total_vitamin_a = sum(f.vitamin_a for f in feedings)
        total_vitamin_c = sum(f.vitamin_c for f in feedings)

        # Find NutrientGoal for baby's age or closest lower age
        age_months = baby.age_in_months  # You need to add age_in_months to Baby model or calculate here
        try:
            goal = NutrientGoal.objects.filter(age_in_months__lte=age_months).order_by('-age_in_months').first()
        except NutrientGoal.DoesNotExist:
            return Response({"error": "No nutrient goal found for this age"}, status=404)
        
        # Calculate % of goal
        def safe_pct(value, goal_value):
            return (value / goal_value * 100) if goal_value > 0 else 0
        
        data = {
            'calories': total_calories,
            'protein': total_protein,
            'fat': total_fat,
            'carbs': total_carbs,
            'vitamin_a': total_vitamin_a,
            'vitamin_c': total_vitamin_c,
            'calories_pct': safe_pct(total_calories, goal.calories),
            'protein_pct': safe_pct(total_protein, goal.protein),
            'fat_pct': safe_pct(total_fat, goal.fat),
            'carbs_pct': safe_pct(total_carbs, goal.carbs),
            'vitamin_a_pct': safe_pct(total_vitamin_a, goal.vitamin_a),
            'vitamin_c_pct': safe_pct(total_vitamin_c, goal.vitamin_c),
        }
        serializer = DailyNutrientSummarySerializer(data)
        return Response(serializer.data)
