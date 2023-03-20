from django.db.models import F
from django.views.generic import RedirectView

from .models import ShortLink


def get_full_url(short_url: str) -> str:
    try:
        short_link = ShortLink.objects.get(short_url__exact=short_url)
        if not short_link.is_active:
            raise KeyError('Token is no longer available')
    except ShortLink.DoesNotExist:
        raise KeyError('We do not know this URL. Try something else')
    short_link.requests_count = F('requests_count') + 1
    return short_link.full_url


class ShortLinkRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        b = 1
        return get_full_url(kwargs.get('short_url'))
