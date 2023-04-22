from django.shortcuts import render

def get_my_portfolio(request):
    return render(request, 'pf/portfolio.html')
