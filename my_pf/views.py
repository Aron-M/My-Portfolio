from django.shortcuts import render
from .models import PersonalDetails, Headings, Project, Skill, SkillCategory


def display_skills_page(request):
    return render(request, 'pages/skills.html')

def display_all(request):
    data = PersonalDetails.objects.all()
    skill = Skill.objects.all()
    category = SkillCategory.objects.all()
    project = Project.objects.all()
    headings = Headings.objects.all()
    context = {
        'data': data, 'headings': headings, 'project': project, 'skill': skill, 'category': category
        }
    if request.path == "/":
        return render(request, 'pages/home-page.html', context )

