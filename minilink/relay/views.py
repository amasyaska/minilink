from django.shortcuts import get_object_or_404, redirect
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UrlSerializer
from .models import URL

class HomePage(APIView):
    def get(self, request):
        popular_links = UrlSerializer(URL.popular.all(), many=True).data
        return Response(popular_links)


class CreateLink(APIView):
    def post(self, request):
        long_url = request.data['longUrl']
        try:
            new_url = URL(long_url=long_url)
            new_url.save()
            return Response({'short_url': new_url.short_url})
        except IntegrityError:
            url = URL.objects.get(long_url=long_url)
            return Response({'short_url': url.short_url})
        

class RedirectTo(APIView):
    def get(self, request):
        url = get_object_or_404(URL, short_url=request.data['shortUrl'])
        url.clicks += 1
        url.save()
        return redirect(url.long_url)