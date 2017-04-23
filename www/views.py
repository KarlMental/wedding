from django.shortcuts import render
from .forms import GuestForm

# Create your views here.
def index(request):
    if (request.method == 'POST'):
        form = GuestForm(data=request.POST)
        if form.is_valid:
            form.save()
    else:
        form = GuestForm()
    return render(request, 'index.html', {'form':form})