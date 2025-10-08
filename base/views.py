from django.shortcuts import render
from jobs.views import featured_jobs
from jobs.models import Category

# Create your views here.
def home_page(request):
    # logos for infinite loop
    logos = [
        'base/images/logo-visa.svg',
        'base/images/logo-toyota.svg',
        'base/images/logo-google.svg',
        'base/images/logo-paypal.svg',
        'base/images/logo-netflix.svg',
        'base/images/logo-adidas.svg',
        'base/images/logo-abbott.svg',
        'base/images/logo-fedex.svg',
    ]

    # top categories for jobs
    # top_categories = [
    #     {
    #         "name" : "Web Development",
    #         "image" : "base/images/category-development.webp",
    #         "jobs_available" : 17
    #     },
    #     {
    #         "name" : "UX/UI Design",
    #         "image" : "base/images/category-ux_ui.webp",
    #         "jobs_available" : 8
    #     },
    #     {
    #         "name" : "Data Science",
    #         "image" : "base/images/category-data-science.webp",
    #         "jobs_available" : 9
    #     },
    #     {
    #         "name" : "Smart AI Services",
    #         "image" : "base/images/category-AI.webp",
    #         "jobs_available" : 7
    #     },
    #     {
    #         "name" : "Digital Marketing",
    #         "image" : "base/images/category-digital marketing.webp",
    #         "jobs_available" : 12
    #     },
    #     {
    #         "name" : "Mobile App Development",
    #         "image" : "base/images/category-mobile-app.webp",
    #         "jobs_available" : 8
    #     }
    # ]


    # fetch categories dynamically
    top_categories = Category.objects.all()
    for cat in top_categories:
        cat.jobs_available = cat.jobs.count()

    # featued jobs
    featured = featured_jobs(request)

    context = {
        "logos" : logos,
        "top_categories" : top_categories,
        "featured_jobs" : featured
    }

    return render(request, "base/index.html", context)