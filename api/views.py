from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import ShortLinkSerializer


class ShortLinkApiView(APIView):

    def post(self, request):
        serializer = ShortLinkSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            short_link = serializer.get_or_create(validated_data=serializer.validated_data)
            return Response(ShortLinkSerializer(short_link).data, status=201)
        return Response(serializer.errors, status=400)

