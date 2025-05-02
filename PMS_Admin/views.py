from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard_view(request):
    # In a real app, you might pull these stats from your database
    context = {
        "sales": 0,
        "purchase": 0,
    }
    return render(request, "dashboard.html", context)
