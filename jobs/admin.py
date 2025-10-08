from django.contrib import admin
from .models import Job, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Job)
class JObAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "category", "featured", "application_deadline")
    list_filter = ("featured", 'category', 'job_type')
    search_fields = ("title", "company")