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




