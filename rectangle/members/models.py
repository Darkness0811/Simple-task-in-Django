from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)


    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.joined_date}"


class Rectangle(models.Model):
    length = models.IntegerField()
    width = models.IntegerField()

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"
    
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

@receiver(post_save, sender=Member)
def members_list_saved(sender, instance, created, **kwargs):
    print("Signal handler started")
    time.sleep(5)  # Simulate a long task
    print(f"{sender},{instance.firstname} details has been saved! Created: {created}")
    
@receiver(post_save, sender=Rectangle)
def fail_signal(sender, instance, created, **kwargs):
    print("Signal running... About to raise an error!")
    raise Exception("Oops! Signal failed.")