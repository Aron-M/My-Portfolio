from django.shortcuts import render
from .models import PersonalDetails

def get_my_portfolio(request):
    return render(request, 'pf/home_page.html')

def display_personal_details(request):
    data = PersonalDetails.objects.all()
    print(data)
    context = {
        'data': data
        }
    return render(request, 'pf/personal_details.html', context)

def display_skills_page(request):
    return render(request, 'pf/skills.html')



