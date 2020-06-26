from django.shortcuts import render
from rest_framework import viewsets, status
from .models import City, Review
from .serializers import CitySerializer, ReviewSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class CitiesView(viewsets.ViewSet):
    
    def list(self, request):
        queryset = City.objects.all()
        data = CitySerializer(queryset, many=True)
        return Response(data.data)

    def create(self, request):
        return Response('Create')

    def retrieve(self, request, pk=None):
        queryset = City.objects.get(name=pk)
        data = CitySerializer(queryset)
        return Response(data.data)

    def put(self, request, pk=None):
        return Response('Update')

    def patch(self, request, pk=None):
        return Response('Partial Update')

class ReviewsView(viewsets.ViewSet):
    
    def list(self, request):
        queryset = Review.objects.raw("SELECT re.id, re.traveller, re.review, re.city, CASE WHEN (re.image = '') IS NOT FALSE THEN ci.image ELSE re.image END as image FROM reviews_review as re JOIN reviews_city as ci on (re.city = ci.name)")
        data = ReviewSerializer(queryset, many=True)
        return Response(data.data)

    def create(self, request):
        return Response('Create')

    def retrieve(self, request, pk=None):
        queryset = Review.objects.get(name=pk)
        data = ReviewSerializer(queryset)
        return Response(data.data)

    def put(self, request, pk=None):
        return Response('Update')

    def patch(self, request, pk=None):
        return Response('Partial Update')
