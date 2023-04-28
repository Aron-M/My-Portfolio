from django.shortcuts import render,  redirect, get_object_or_404
from .models import PersonalDetails

def get_my_portfolio(request):
    return render(request, 'pf/personal_details.html')

def personal_details(request):
    data = PersonalDetails.objects.all()
    context = {
        'data': data
        }
    return render(request, 'my_pf/templates/pf/personal_details.html' , context)





