from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views import VacancyViewSet, CompanyViewSet, HardskilsViewSet
app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register('vacancy', VacancyViewSet, basename='vacancys')
router_v1.register('company', CompanyViewSet, basename='companys')
router_v1.register('hardskils', HardskilsViewSet, basename='tag')

urlpatterns = [
    path('', include(router_v1.urls)),
]
