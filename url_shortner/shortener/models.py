from django.db import models
import string, random

def generate_short_code():
    length = 6
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

class URL(models.Model):
    long_url = models.URLField()
    short_code = models.CharField(max_length=6, unique=True, default=generate_short_code)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.short_code} -> {self.long_url}"
class URL(models.Model):
    original_url = models.URLField()
    short_id = models.CharField(max_length=10, unique=True)
    clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.short_id} -> {self.original_url}"
