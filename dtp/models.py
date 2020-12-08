from django.db import models
from django.contrib.auth.models import User


class DoctorTitle(models.Model):
    full = models.CharField(max_length=30)
    short = models.CharField(max_length=10)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.OneToOneField(DoctorTitle, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.get_full_name()


class Examination(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    description = models.TextField(max_length=350)
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ExaminationPhoto(models.Model):
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.image
