import random

from django.conf import settings
from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.response import Response

from api.models import ShortLink



class ShortLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortLink
        fields = '__all__'
        extra_kwargs = {'full_url': {'validators': []}}

    def get_or_create(self, validated_data):
        full_url = validated_data.get('full_url')
        short_url = validated_data.get('short_url')

        short_link = ShortLink.objects.filter(full_url=full_url)
        if not short_link.exists():
            if not short_url:
                while True:
                    short_url = ''.join(random.choices(settings.CHARACTERS, k=settings.TOKEN_LENGTH))
                    try:
                        short_link = ShortLink.objects.create(full_url=full_url, short_url=short_url)
                    except IntegrityError:
                        continue
                    else:
                        return short_link

            try:
                short_link = ShortLink.objects.create(full_url=full_url, short_url=short_url)
            except IntegrityError:
                return Response('This url is not available, try something else', status=400)
            else:
                return short_link
        return short_link.first()


