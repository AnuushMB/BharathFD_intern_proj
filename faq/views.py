from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer
from django.http import HttpResponse

class FAQViewSet(viewsets.ViewSet):

    def home(self, request):
        return HttpResponse("<h1>Welcome to the FAQ API</h1><p>Go to <a href='/api/faqs/'>API Endpoint</a></p>")

    def list(self, request):
        
        lang = request.GET.get('lang', 'en')  # Default to English
        faqs = FAQ.objects.all()
        data = [faq.get_translated_faq(lang) for faq in faqs]
        return Response(data)

