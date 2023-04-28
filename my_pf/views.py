from django.shortcuts import render, redirect
from .models import PersonalDetails

def get_my_portfolio(request):
    return render(request, 'pf/personal_details.html')

def personal_details(request):
    data = PersonalDetails.objects.all()
    context = {'datas': data}
    return render(request, 'personal_details.html', context)

def add_personal_details(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        age = request.POST['age']
        nationality = request.POST['nationality']
        residency = request.POST['residency']
        languages = request.POST['languages']
        address = request.POST['address']
        details = PersonalDetails.objects.create(
            full_name=full_name,
            age=age,
            nationality=nationality,
            residency=residency,
            languages=languages,
            address=address
        )
        details.save()
        return redirect('personal_details')
    else:
        return render(request, 'add_personal_details.html')


def personal_details(request):
    latest_personal_details = PersonalDetails.objects.latest('id')
    context = {
        'personal_details': latest_personal_details
    }
    return render(request, 'personal_details.html', context)
