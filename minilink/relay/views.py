from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from models import URL

class CreateLink(APIView):
    def post(self, request):
        long_url = request.POST.get('longUrl')
        if long_url:
            new_url = URL(long_url)
            return Response({'status': 'ok', 
                            'short_url': new_url.short_url})
        return Response({'status': 'error'})