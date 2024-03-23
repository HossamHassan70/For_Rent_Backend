from django.db import models
from datetime import datetime, timedelta
import random
from django.db import models
from django.core.mail import send_mail


class UserEmailVerification(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=6, default=000000)
    expireTime = models.DateTimeField()

    def __str__(self):
        return f"{self.email} | {self.code} | expires: {self.expireTime}"

    def sendCode(self):
        send_mail(
            subject="Welcome to the platform",
            message=f"Thank you for signing up to our platform\nYour verification code is: {self.code}",
            from_email="noreply@myrent.com",
            recipient_list=[self.email],
            fail_silently=False,
        )

    def generateCode(self):
        self.code = random.randint(100000, 999999)
        self.expireTime = datetime.now() + timedelta(days=1)
        self.save()

