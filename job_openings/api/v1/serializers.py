from rest_framework import serializers

from app_hr.models import Hardskils, Vacancy, Company


class HardskilsSerializer(serializers.ModelSerializer):
    """Сереалайзер тегов."""

    class Meta:
        model = Hardskils
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    """Сереалайзер вакансии для гет запроса"""
    class Meta:
        model = Company
        fields = '__all__'


class VacansiSerializer(serializers.ModelSerializer):
    """Сереалайзер вакансии для гет запроса"""
    class Meta:
        model = Vacancy
        fields = '__all__'
        fields = (
            "dateIns",
            "name",
            "description",
            "min_salary",
            "max_salary",
            "location",
            "employmentType",
            "phone",
            "email",
            "city",
            "employer",
            "specialty",
        )
