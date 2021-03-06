from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import AddForm


def index(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:
        form = AddForm()
    return render(request, 'tools/index.html', {'the_form':form})