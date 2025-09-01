from django.test import TestCase
from core.models import FeedingRecord, FoodItem, Baby, Caregiver
from django.contrib.auth.models import User
from datetime import datetime

class FeedingRecordTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        caregiver = Caregiver.objects.create(user=user)
        baby = Baby.objects.create(name="Test Baby")
        food = FoodItem.objects.create(name='Milk', calories_per_100ml=67, protein_per_100ml=1.3)
        self.caregiver = caregiver
        self.baby = baby
        self.food = food

    def test_feeding_creation(self):
        feeding = FeedingRecord.objects.create(
            baby=self.baby,
            caregiver=self.caregiver,
            food_item=self.food,
            amount_ml=150,
            fed_at=datetime.now()
        )
        self.assertAlmostEqual(feeding.calories, 150 * 67 / 100)
        self.assertAlmostEqual(feeding.protein, 150 * 1.3 / 100)
