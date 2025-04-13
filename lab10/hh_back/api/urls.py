from django.urls import path, include

from .views import company_detail, vacancies_by_company, vacancy_list, VacancyDetailApiView, top_ten_vacancies, \
    CompanyListApiView, CompanyList

urlpatterns = [
    path('companies/', CompanyList.as_view()),
    path('companies/<int:id>/', company_detail),
    path('companies/<int:id>/vacancies/', vacancies_by_company),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:id>/',VacancyDetailApiView.as_view()),
    path('vacancies/top_ten/', top_ten_vacancies),
]