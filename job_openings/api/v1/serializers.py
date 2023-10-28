from rest_framework import serializers

from app_hr.models import Education, Hardskils, JobExpiriense, ProjectActivities, SpecializationType, Specialty, Vacancy, Company, Employment


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


class EducationSerializer(serializers.ModelSerializer):
    """Сериализатор образования."""

    class Meta:
        model = Education
        fields = (
            'name_education',
        )


class JobExperienceSerializer(serializers.ModelSerializer):
    """Сериализатор опыта работы."""

    class Meta:
        model = JobExpiriense
        fields = ('jobexpiriense',)


class ProjectActivitiesSerializer(serializers.ModelSerializer):
    """Сериализатор проектных активностей."""

    class Meta:
        model = ProjectActivities
        fields = (
            'projectActivities',
        )


class SpecializationTypeSerializer(serializers.ModelSerializer):
    """Сериализатор типа специализации."""

    class Meta:
        model = SpecializationType
        fields = (
            'specializationType',
        )


class SpecialtySerializer(serializers.ModelSerializer):
    """Сериализатор специальности."""

    class Meta:
        model = Specialty
        fields = (
            'specialty',
        )


class EmploymentTypeSerializer(serializers.ModelSerializer):
    """Сериализатор типа занятости."""

    class Meta:
        model = Employment
        fields = ('name_employment',)


class VacansiSerializer(serializers.ModelSerializer):
    """Сереалайзер вакансии для гет запроса"""
    author_vacancy = CompanySerializer()
    education = EducationSerializer()
    employmentType = EmploymentTypeSerializer()
    jobexpiriense = JobExperienceSerializer()
    projectActivities = ProjectActivitiesSerializer()
    specializationType = SpecializationTypeSerializer()
    specialty = SpecialtySerializer()
    keyskils = HardskilsSerializer(many=True)

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
