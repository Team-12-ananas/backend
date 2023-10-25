from rest_framework.serializers import ModelSerializer

from app_hr.models import Hardskils


class TagSerializer(ModelSerializer):
    """Сереалайзер тегов."""

    class Meta:
        model = Hardskils
        fields = '__all__'

