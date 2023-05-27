from django.shortcuts import render, get_object_or_404, redirect
from .models import PersonalDetails, Headings, Project, Skill, SkillCategory
from .forms import PersonalDetailsForm, HeadingsForm

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




def display_edit_personal_details(request):
    data = PersonalDetails.objects.all()
    personal_details_form = PersonalDetailsForm()
    detail = get_object_or_404(PersonalDetails)
    if request.method == 'POST':
        personal_details_form = PersonalDetailsForm(request.POST, instance=detail)
        if personal_details_form.is_valid():
            personal_details_form.save()
            return redirect('edit-personal-details')
    personal_details_form = PersonalDetailsForm(instance=detail)
    context = {
        'data': data, 'personal_details_form': personal_details_form
        }
    if request.path == "edit-personal-details/":
        return render(request, 'pages/edit-personal-details.html', context )
    else: 
                return render(request, 'pages/edit-personal-details.html', context )


def display_edit_headings(request):
    all_headings = Headings.objects.all()
    headings_form = HeadingsForm()
    heading = get_object_or_404(Headings)
    if request.method == 'POST':
        headings_form = HeadingsForm(request.POST, instance=heading)
        if headings_form.is_valid():
            headings_form.save()
            return redirect('edit-headings')
    headings_form = HeadingsForm(instance=heading)
    context = {
        'headings': all_headings,
        'headings_form': headings_form
    }
    if request.path == "edit-headings/":
        return render(request, 'pages/edit-headings.html', context)
    else: 
        return render(request, 'pages/edit-headings.html', context)

