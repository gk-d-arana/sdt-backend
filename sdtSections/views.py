from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *


@api_view(['GET'])
def get_all_main_sections_view(request):
    MainSections = MainSection.objects.all()
    serializer = MainSectionSerializer(MainSections, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_sections_view(request, pk):
    try:
        main_section = MainSection.objects.get(pk=pk)
        Sections = Section.objects.filter(main_section=main_section)
        serializer = SectionSerializer(Sections, many=True)
        return Response(serializer.data)
    except Exception:
        return JsonResponse({'error': 'No Such Main Section'})


@api_view(['GET'])
def get_all_products_view(request, pk):
    try:
        section = Section.objects.get(pk=pk)
        Products = Product.objects.filter(section=section)
        serializer = ProductsSerializer(Products, many=True)
        return Response(serializer.data)
    except Exception:
        return JsonResponse({'error': 'No Such Section'})

