from django.shortcuts import render, redirect
from .forms import BehindForm
from .models import Behind


# Create your views here.
def index(request):
    behinds = Behind.objects.all()
    context = {
        'behinds': behinds,
    }
    return render(request, 'behinds/index.html', context)

def create(request):
    if request.method == "POST":
        form = BehindForm(request.POST)
        if form.is_valid():
            behind = form.save(commit=False)
            behind.user = request.user
            behind.save()
            return redirect('behinds:index')

    else:
        form = BehindForm()
        context = {
            'form' : form
        }
        return render(request, 'behinds/create.html', context)
