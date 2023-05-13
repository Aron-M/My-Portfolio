from django.shortcuts import render
from .models import PersonalDetails, Language, Framework, Library, VersionControl, Database


def display_skills_page(request):
    return render(request, 'pages/skills.html')

def display_all(request):
    data = PersonalDetails.objects.all()
    print(data)
    context = {
        'data': data
        }
    if request.path == "/":
        return render(request, 'pages/home_page.html', context )
    else:
        return render(request, 'pages/personal_details.html', context)


# def display_skills_model(request):
#     data = Skills.objects.all()
#     print(data)
#     context = {
#         'data': data
#         }
#     return render(request, 'pages/skills.html', context)


def skills(request):
    languages = Language.objects.all()
    frameworks = Framework.objects.all()
    libraries = Library.objects.all()
    versioncontrol = VersionControl.objects.all()
    database = Database.objects.all()
    return render(request, 'my_pf/templates/pages/home_page.html', {'languages': languages, 'frameworks': frameworks, 'libraries': libraries, 'versioncontrol': versioncontrol, 'database': database})


