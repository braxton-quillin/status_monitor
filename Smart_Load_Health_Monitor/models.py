from django.db import models


class Appliance(models.Model):

    # required
    appliance = models.CharField(max_length=255)
    service_date = models.DateField(null=True, blank=True)
    # optional fields
    model = models.CharField(max_length=255, null=True, blank=True)
    serial = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    kit = models.CharField(max_length=255, null=True, blank=True)
    # optional, num of days between each service if repeating
    service_repeat = models.IntegerField(null=True, blank=True)

    # internal
    notified = models.BooleanField(default=False)

    def __str__(self):
        return self.appliance
