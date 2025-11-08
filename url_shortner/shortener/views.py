from django.shortcuts import render, get_object_or_404, redirect
from .models import URL
import string, random

def home(request):
    short_url = None
    if request.method == 'POST':
        original_url = request.POST['original_url']
        short_id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        url = URL.objects.create(original_url=original_url, short_id=short_id)
        short_url = request.build_absolute_uri('/') + short_id
    urls = URL.objects.all()  
    return render(request, 'shortener/home.html', {'short_url': short_url, 'urls': urls})

# Redirect view with click tracking
def redirect_short_url(request, short_id):
    url = get_object_or_404(URL, short_id=short_id)
    url.clicks += 1
    url.save()
    return redirect(url.original_url)
