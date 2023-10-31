from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from app_hr.models import Hardskils, Vacancy, Company
from api.v1.serializers import (HardskilsSerializer, VacancyCreateSerializer,
                                VacancySerializer,
                                CompanySerializer)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action


class HardskilsViewSet(ReadOnlyModelViewSet):
    """Вьюсет тегов."""

    queryset = Hardskils.objects.all()
    serializer_class = HardskilsSerializer
    permission_classes = (AllowAny,)
    pagination_class = None


class VacancyViewSet(ModelViewSet):
    """Вьюсет вакансий."""

    queryset = Vacancy.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return VacancySerializer
        elif self.action == 'create':
            return VacancyCreateSerializer
        return VacancySerializer

    @staticmethod
    def adding_author(add_serializer, model, request, company_id, vacancy_id):
        """Пользовательский метод добавления компании в качестве автора и извлечения данных"""
        company = Company.objects.get(id=company_id)
        vacancy = Vacancy.objects.get(id=vacancy_id)
        data = {'company': company.id, 'vacancy': vacancy.id}
        serializer = add_serializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.to_representation(serializer.instance),
            status=status.HTTP_201_CREATED,
        )

    @action(
        detail=False, methods=['get'], permission_classes=(AllowAny,)
    )
    def arhive(self, request):
        """Возвращает пользователей, на которых подписан текущий пользователь.
        В выдачу добавляются рецепты.
        """
        return self.get_paginated_response(
            CompanySerializer(
                self.paginate_queryset(
                    Company.objects.filter(subscribing__user=request.user)
                ),
                many=True,
                context={'request': request},
            ).data
        )


class CompanyViewSet(ReadOnlyModelViewSet):
    """Вьюсет тегов."""

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    http_method_names = ['get']

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CompanySerializer
        company_instance = self.get_object()
        company_serializer = self.get_serializer(company_instance)
        vacancies_queryset = Vacancy.objects.filter(
            author_vacancy=company_instance)
        vacancies_serializer = VacancySerializer(vacancies_queryset, many=True)
        response_data = {
            'company': company_serializer.data,
            'vacancies': vacancies_serializer.data
        }
        return Response(response_data)
