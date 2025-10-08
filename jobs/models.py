from django.db import models
from datetime import date, timedelta


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.description}"


class Job(models.Model):
    JOB_TYPES = (
        ("FT", "Full-Time"),
        ("PT", "Part-Time"),
        ("IN", "Internship"),
        ("RE", "Remote"),
    )

    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=2, choices=JOB_TYPES, default="FT")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="jobs", null=True, blank=True) # link
    salary = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    logo = models.ImageField(upload_to="jobs/logos/", blank=True, null=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    application_deadline = models.DateField(default=date.today() + timedelta(days=30))

    def day_left(self):
        delta = self.application_deadline - date.today()
        return max(delta.days, 0)

    def __str__(self):
        return f"{self.title} ({self.company})"