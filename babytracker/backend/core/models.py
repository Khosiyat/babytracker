from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Baby(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    caregivers = models.ManyToManyField(User)

    def age_in_months(self):
        today = date.today()
        return (today.year - self.birth_date.year) * 12 + today.month - self.birth_date.month


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    calories_per_100ml = models.FloatField()
    protein_per_100ml = models.FloatField()
    is_custom = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)


class FeedingRecord(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    caregiver = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    amount_ml = models.FloatField()
    fed_at = models.DateTimeField(auto_now_add=True)

    calories = models.FloatField()
    protein = models.FloatField()

    def save(self, *args, **kwargs):
        self.calories = self.amount_ml * self.food_item.calories_per_100ml / 100
        self.protein = self.amount_ml * self.food_item.protein_per_100ml / 100
        super().save(*args, **kwargs)

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    calories_per_100ml = models.FloatField()
    protein_per_100ml = models.FloatField()
    
    fat_per_100ml = models.FloatField(default=0.0)
    carbs_per_100ml = models.FloatField(default=0.0)
    vitamin_a_per_100ml = models.FloatField(default=0.0)
    vitamin_c_per_100ml = models.FloatField(default=0.0)
    # Add more vitamins/minerals as needed
    
    is_custom = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name



class NutrientGoal(models.Model):
    age_in_months = models.PositiveIntegerField()
    
    # Daily target nutrient values
    calories = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()
    vitamin_a = models.FloatField()
    vitamin_c = models.FloatField()
    # Add more goals as needed

    def __str__(self):
        return f"Goals for {self.age_in_months} month(s)"
