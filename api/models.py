from django.db import models


class ShortLink(models.Model):
    full_url = models.URLField(unique=True)
    short_url = models.CharField(max_length=10, unique=True, db_index=True, blank=True)
    request_count = models.IntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_date',)