from django.db import models


class Appliance(models.Model):

    appliance = models.CharField(max_length=255)
    model = models.CharField(max_length=255, null=True, blank=True)
    serial = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    kit = models.CharField(max_length=255, null=True, blank=True)
    service_date = models.DateField(null=True, blank=True)
    service_repeat = models.IntegerField(null=True, blank=True)

    notified = models.BooleanField(default=False)

    def __str__(self):
        return self.appliance
