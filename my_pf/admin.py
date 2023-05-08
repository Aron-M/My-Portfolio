from django.contrib import admin
from .models import PersonalDetails, Skills, Language, Framework, Library, VersionControl


admin.site.register(PersonalDetails)
admin.site.register(Skills)
admin.site.register(Language)
admin.site.register(Framework)
admin.site.register(Library)
admin.site.register(VersionControl)