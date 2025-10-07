from django.shortcuts import render

# Create your views here.
def jobs_by_category(request):
    return render(request, "jobs/jobs_by_category.html")