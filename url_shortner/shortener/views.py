from django.shortcuts import render, redirect, get_object_or_404
from .models import URL

def home(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        url_obj, created = URL.objects.get_or_create(long_url=long_url)
        return render(request, 'shortener/home.html', {'short_url': request.build_absolute_uri('/') + url_obj.short_code})
    return render(request, 'shortener/home.html')

def redirect_url(request, short_code):
    url_obj = get_object_or_404(URL, short_code=short_code)
    return redirect(url_obj.long_url)
