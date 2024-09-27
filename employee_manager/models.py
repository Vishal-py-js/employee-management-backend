from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.TextField(max_length=100, null=False, blank=False)
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


