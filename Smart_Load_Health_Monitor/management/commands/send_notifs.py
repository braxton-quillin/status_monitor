import notifier.utils
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from Smart_Load_Health_Monitor.models import Appliance
from datetime import timedelta


class Command(BaseCommand):
    help = "send notifications for service"

    def handle(self, *args, **kwargs):
        today = timezone.now().date()

        appliances = Appliance.objects.filter(service_date=today, notified=False)

        # testing
        self.stdout.write(self.style.SUCCESS(f"Attempting to send emails"))

        for appliance in appliances:
            try:
                notifier.utils.send_demo_email()

                if appliance.service_repeat != None:
                    appliance.notified = True
                else:
                    appliance.service_date += timedelta(days=appliance.service_repeat)
                appliance.save()

                self.stdout.write(self.style.SUCCESS(f"Sent email"))

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Failed to send email for {appliance.appliance}")
                )
