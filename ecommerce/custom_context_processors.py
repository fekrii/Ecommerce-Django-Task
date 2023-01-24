from notifications.models import OrderNotification

def notifications(request):
    notifications = OrderNotification.objects.all()
    return {"notifications": notifications}