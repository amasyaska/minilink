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
        url = request.data['longUrl']
        # if certain long url already exists in db, return its short representation
        # otherwise create new row in db with this url and its representation
        try:
            while True:
                # loop to check collisions: if long url with this short representation
                # already exists in db, then one more representation is generated
                new_url = URL.objects.create(url=url)
                if len(URL.objects.filter(short=new_url.short)) == 1:
                    break
            return Response({'short': new_url.short})
        except IntegrityError:
            existing_url = URL.objects.get(url=url)
            return Response({'short': existing_url.short})


class RedirectTo(APIView):
    def get(self, request, short_link):
        url = get_object_or_404(URL, short=short_link)
        url.visits += 1
        url.save()
        return redirect(url.url)