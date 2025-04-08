from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Member
import time

@receiver(post_save, sender=Member)
def members_list_saved(sender, instance, created, **kwargs):
    print("Signal handler started")
    time.sleep(5)  # Simulate a long task
    print(f"{instance.firstname} details has been saved! Created: {created}")