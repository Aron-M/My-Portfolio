from django.shortcuts import render
from .models import PersonalDetails


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