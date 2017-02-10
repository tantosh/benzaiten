from django.shortcuts import render
from forms import SummaryForm

def index(request):
    if request.method == 'POST':
        form = SummaryForm(request.POST)
        if form.is_valid():
            summary = 'this is a sample summary'
            return render(request, 'index.html', {'summary': 
                                                 summary = 'this is a sample summary'})
    else:
        form = SummaryForm()
    return render(request, 'index.html', {'form': form })