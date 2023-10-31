import datetime
from django.utils import timezone
from django.db import models
from simple_history.models import HistoricalRecords


class TimeStamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Circle(TimeStamps):
    circle_name = models.CharField(max_length=200)
    history = HistoricalRecords(excluded_fields=['created_at'])

    def __str__(self):
        return self.circle_name


class Kpi(TimeStamps):
    month_choice = [(1, "Jan"), (2, "Feb"), (3, "Mar"),
                    (4, "Apr"), (5, "May"), (6, "Jun"),
                    (7, "Jul"), (8, "Aug"), (9, "Sep"),
                    (10, "Oct"), (11, "Nov"), (12, "Dec")]

    circle = models.ManyToManyField(Circle, blank=True)
    kpi_name = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    year = models.IntegerField(default=2023)
    month = models.IntegerField(choices=month_choice, default=1)
    updated_by = models.CharField(max_length=200)
    history = HistoricalRecords(excluded_fields=['kpi_name', 'created_at'])

    def __str__(self):
        return self.kpi_name

