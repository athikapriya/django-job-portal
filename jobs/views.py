from django.shortcuts import render
from .models import Job, Category

# Create your views here.
def jobs_by_category(request):
    return render(request, "jobs/jobs_by_category.html")

def featured_jobs(request):
    featured_jobs = Job.objects.filter(featured=True).order_by("created_at")[:12]
    return featured_jobs

def all_jobs(request):
    jobs = Job.objects.all().order_by("_created_at")
    return render(request, "jobs/all_jobs.html", {"jobs" : jobs})