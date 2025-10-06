from django.shortcuts import render

# Create your views here.
def home_page(request):
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
    return render(request, "base/index.html", {"logos" : logos})