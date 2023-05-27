from django.shortcuts import render, get_object_or_404, redirect
from .models import PersonalDetails, Headings, Project, Skill, SkillCategory
from .forms import PersonalDetailsForm

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
    if request.path == "home/":
        return render(request, 'pages/home-page.html', context )
    else: 
        return render(request, 'pages/home-page.html', context )

def dashboard_view(request):
    return render(request, 'pages/dashboard.html')


def dashboard(request):
    personal_details = PersonalDetails.objects.all()
    details_form = PersonalDetailsForm()

    if request.method == 'POST':
        details_form = DetailsForm(request.POST)
        if details_form.is_valid():
            details_form.save()
            return redirect('dashboard/edit-top')

    context = {
        'details': details,
        'details_form': details_form,
        }
    return render(request, 'pages/dashboard.html', context)



def display_edit_top(request):
    data = PersonalDetails.objects.all()
    personal_details_form = PersonalDetailsForm()
    detail = get_object_or_404(PersonalDetails)
    if request.method == 'POST':
        personal_details_form = PersonalDetailsForm(request.POST, instance=detail)
        if personal_details_form.is_valid():
            personal_details_form.save()
            return redirect('edit-top')
    personal_details_form = PersonalDetailsForm(instance=detail)
    context = {
        'data': data, 'personal_details_form': personal_details_form
        }
    if request.path == "edit-top/":
        return render(request, 'pages/edit-top.html', context )
    else: 
                return render(request, 'pages/edit-top.html', context )