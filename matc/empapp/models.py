import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models


class EmployeeUserAuth(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.CharField(max_length=100, unique=True)
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    password = models.CharField(max_length=2000, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    emp_position = models.CharField(max_length=50)
    emp_salary = models.CharField(max_length=50)
    emp_experience = models.CharField(max_length=50)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    emp_id = models.ForeignKey(EmployeeUserAuth, on_delete=models.CASCADE)
    companyname = models.CharField(max_length=250, null=True, blank=True)
    phonenumber = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    emp_id = models.ForeignKey(EmployeeUserAuth, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    DOB = models.IntegerField(default=0)










