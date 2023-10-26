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
    name = serializers.CharField(source='get_name_display')
    location = serializers.CharField(source='get_location_display')
    employmentType = serializers.CharField(source='get_employmentType_display')
    employer = serializers.SerializerMethodField()
    specialty = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Vacancy
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

    def get_employer(self, obj):
        return obj.employer.get_name_company_display()
