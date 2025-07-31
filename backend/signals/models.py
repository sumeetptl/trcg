from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Signal(models.Model):
    DIRECTION_CHOICES = [
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    ]

    coin = models.CharField(max_length=10)
    direction = models.CharField(max_length=5, choices=DIRECTION_CHOICES)
    entry_price = models.DecimalField(max_digits=10, decimal_places=2)
    leverage = models.PositiveSmallIntegerField()
    targets = models.JSONField()  # e.g. {"42000": "pending", "45000": "hit"}
    stop_loss = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.coin} {self.direction} @ {self.entry_price}"
