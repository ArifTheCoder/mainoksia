from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from datetime import date
from .serializers import CompanySerializer, ImageSerializer
from .models import Company, Image

# Create your views here.
class CompanyList(generics.ListAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        return Company.objects.all()


class GetMainoksiaForCompany(generics.ListAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        current_week_number = date.today().isocalendar()[1]
        
        image_instances = Image.objects.filter(week__company__pk=self.kwargs["company_id"], week__week_number=current_week_number)

        if not image_instances:
            last_week_number_to_check = current_week_number - 4

            while current_week_number >= last_week_number_to_check:
                if (current_week_number > 0):
                    image_instances = Image.objects.filter(week__company__pk=self.kwargs["company_id"], week__week_number=current_week_number)

                    if (len(image_instances) > 0):
                        break
                current_week_number -= 1

        return image_instances
