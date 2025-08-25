from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodItemViewSet, FeedingRecordViewSet, baby_daily_summary

router = DefaultRouter()
router.register(r'food-items', FoodItemViewSet)
router.register(r'feedings', FeedingRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('baby/<int:baby_id>/summary/', baby_daily_summary),
]
