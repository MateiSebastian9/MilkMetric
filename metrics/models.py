from django.db import models

# Create your models here.
class MilkMetric(models.Model):
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Milk Metric: {self.amount}kg at {self.timestamp}"
