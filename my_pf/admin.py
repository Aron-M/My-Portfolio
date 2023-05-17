from django.contrib import admin
from .models import PersonalDetails, Skills, Language, Framework, Library, VersionControl, Database, Home


admin.site.register(PersonalDetails)
admin.site.register(Skills)
admin.site.register(Language)
admin.site.register(Framework)
admin.site.register(Library)
admin.site.register(VersionControl)
admin.site.register(Database)
admin.site.register(Home)