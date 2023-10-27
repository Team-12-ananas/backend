from django.contrib import admin
from .models import (Specialty,
                     SpecializationType,
                     ProjectActivities,
                     JobExpiriense,
                     Education,
                     Employment,
                     Company,
                     Hardskils,
                     Vacancy)

admin.site.register(Specialty)
admin.site.register(SpecializationType)
admin.site.register(ProjectActivities)
admin.site.register(JobExpiriense)
admin.site.register(Education)
admin.site.register(Employment)
admin.site.register(Company)
admin.site.register(Hardskils)
admin.site.register(Vacancy)
