from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class OrderNotification(models.Model):
    message = models.TextField()
    time= models.DateTimeField()
    sent = models.BooleanField(default=False)

    class Meta:
        ordering = ['-time']


@receiver(post_save, sender=OrderNotification)
def notification_handler(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_orderComplete",
        {
            'type': 'send_notification',
            'message': "Your Order added to cart successfuly"
        }
    )