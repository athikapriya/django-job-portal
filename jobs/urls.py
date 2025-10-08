from django.urls import path
from . import views

urlpatterns = [
    path("all-categories", views.jobs_by_category, name="jobs_by_category"), #for jobs by category
    path('', views.all_jobs, name='all_jobs'),
]
