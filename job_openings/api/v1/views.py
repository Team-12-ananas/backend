from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from app_hr.models import Hardskils, Vacancy, Company
from api.v1.serializers import (HardskilsSerializer,
                                VacansiSerializer,
                                CompanySerializer)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


class HardskilsViewSet(ReadOnlyModelViewSet):
    """Вьюсет тегов."""

    queryset = Hardskils.objects.all()
    serializer_class = HardskilsSerializer
    permission_classes = (AllowAny,)
    pagination_class = None


class VacancyViewSet(ModelViewSet):
    """Вьюсет тегов."""

    queryset = Vacancy.objects.all()
    serializer_class = VacansiSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED, headers=headers)


class CompanyViewSet(ReadOnlyModelViewSet):
    """Вьюсет тегов."""

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (AllowAny,)
    pagination_class = None
