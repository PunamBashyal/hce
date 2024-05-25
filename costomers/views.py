from django.shortcuts import redirect, render
from .forms import CostomerSignupForm
from .models import Costomer



def signup(request):
    costomer= None
    if request.method == 'POST':
        form = CostomerSignupForm(request.POST)
        if form.is_valid():
            form.save()
            costomer = Costomer.objects.all()
            return render(request, 'costomers/costomer_details.html', {'costomer':costomer})
    else:
        form= CostomerSignupForm()
    return render(request, 'costomers/signup.html', {'form':form,'costomer':costomer})
    

# Create your views here.
