from django.shortcuts import render
from .models import PersonalDetails, Skills, Headings, Project


def display_skills_page(request):
    return render(request, 'pages/skills.html')

def display_all(request):
    data = PersonalDetails.objects.all()
    skills = Skills.objects.all()
    headings = Headings.objects.all()
    projects = Project.objects.all()
    context = {
        'data': data, 'headings': headings, 'projects': projects, 'skills':skills
        }
    if request.path == "/":
        return render(request, 'pages/home_page.html', context )


# def display_skills_model(request):
#     data = Skills.objects.all()
#     print(data)
#     context = {
#         'data': data
#         }
#     return render(request, 'pages/skills.html', context)
