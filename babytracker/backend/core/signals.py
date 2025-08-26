from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import localtime, now
from .models import FeedingRecord
from datetime import timedelta
from django.core.mail import send_mail

@receiver(post_save, sender=FeedingRecord)
def check_daily_goal(sender, instance, created, **kwargs):
    if not created:
        return

    baby = instance.baby
    today = localtime(now()).date()

    records_today = FeedingRecord.objects.filter(baby=baby, fed_at__date=today)
    milk_ml = sum([r.amount_ml for r in records_today if r.food_item.name.lower() == 'milk'])

    if milk_ml >= 1000:  # Change dynamically based on age if needed
        message = f"✅ {baby.name} has met the milk intake goal today: {milk_ml}ml"
    else:
        message = f"⚠️ {baby.name} has NOT met the milk goal. Only: {milk_ml}ml"

    # Send email to all caregivers
    for caregiver in baby.caregivers.all():
        send_mail(
            f'Daily Feeding Summary for {baby.name}',
            message,
            'noreply@babytracker.com',
            [caregiver.email],
            fail_silently=True
        )
