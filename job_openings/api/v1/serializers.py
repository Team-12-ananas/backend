from rest_framework import serializers

from app_hr.models import Archive, Hardskils, Vacancy, Company
from rest_framework.validators import UniqueTogetherValidator


class HardskilsSerializer(serializers.ModelSerializer):
    """Сереалайзер тегов."""

    class Meta:
        model = Hardskils
        fields = ('name',)


class CompanySerializer(serializers.ModelSerializer):
    """Сереалайзер вакансии для гет запроса"""
    class Meta:
        model = Company
        fields = (
            'name_company',
        )


class VacancySerializer(serializers.ModelSerializer):
    """Сериализатор вакансии для гет запроса"""
    author_vacancy = serializers.StringRelatedField()
    education = serializers.StringRelatedField()
    employmentType = serializers.StringRelatedField(many=True)
    jobexpiriense = serializers.StringRelatedField()
    projectActivities = serializers.StringRelatedField()
    specializationType = serializers.StringRelatedField()
    specialty = serializers.StringRelatedField()
    keyskils = serializers.StringRelatedField(many=True)
    active_vacancy = serializers.ReadOnlyField()

    class Meta:
        model = Vacancy
        fields = (
            "dateIns",
            "city",
            "description",
            "email",
            "min_salary",
            "max_salary",
            "name",
            "phone",
            "author_vacancy",
            "education",
            "employmentType",
            "jobexpiriense",
            "projectActivities",
            "specializationType",
            "specialty",
            "keyskils",
            "active_vacancy",
        )


class VacancyCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания вакансии."""

    class Meta:
        model = Vacancy
        fields = (
            "dateIns",
            "city",
            "description",
            "email",
            "min_salary",
            "max_salary",
            "name",
            "phone",
            "author_vacancy",
            "education",
            "employmentType",
            "jobexpiriense",
            "projectActivities",
            "specializationType",
            "specialty",
            "keyskils",
        )


class PostArhiveSerializer(serializers.ModelSerializer):
    """Сереалайзер избранного"""

    class Meta:
        model = Archive
        fields = ('name_company', 'vacancy')
        validators = [
            UniqueTogetherValidator(
                queryset=Archive.objects.all(),
                fields=['name_company', 'vacancy'],
                message='Вы уже добавили эту вакансию',
            )
        ]

    def to_representation(self, instance):
        request = self.context.get('request')
        return VacancyCreateSerializer(
            instance.recipe, context={'request': request}
        ).data
