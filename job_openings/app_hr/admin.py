from django.contrib import admin
from .models import (Location, Education,
                     Employment, Company, Hardskils, Vacancy)

admin.site.register(Location)
admin.site.register(Education)
admin.site.register(Employment)
admin.site.register(Company)
admin.site.register(Hardskils)
admin.site.register(Vacancy)
