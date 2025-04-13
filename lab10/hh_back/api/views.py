from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status,mixins,generics

from .models import Company, Vacancy
from .serializers import CompanySerializer, VacancySerializer, CompanySerializer2

class CompanyList(generics.ListCreateAPIView):
    serializer_class = CompanySerializer2
    queryset = Company.objects.all()


class CompanyListApiView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

@api_view(["GET"])
def company_detail(request, id):
    company = get_object_or_404(Company, pk=id)
    serializer = CompanySerializer(company)
    return Response(serializer.data)

@api_view(["GET"])

def vacancies_by_company(request, id):
    company = get_object_or_404(Company, pk=id)
    vacancies = company.vacancies.all()
    serializer = VacancySerializer(vacancies, many=True)
    return Response(serializer.data)

@api_view(["GET"])

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    serializer = VacancySerializer(vacancies, many=True)
    return Response(serializer.data)

class VacancyDetailApiView(APIView):
    def get(self, request, id):
        try:
            vacancy = Vacancy.objects.get(id=id)
            serializer = VacancySerializer(vacancy)
            return Response(serializer.data)
        except Vacancy.DoesNotExist as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def top_ten_vacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    serializer = VacancySerializer(vacancies, many=True)
    return Response(serializer.data)
