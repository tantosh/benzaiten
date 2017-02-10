from django.shortcuts import render
from benzaitenweb.forms import SummaryForm
from benzaiten.summarization import TextRankSummarizer

def index(request):
    if request.method == 'POST':
        form = SummaryForm(request.POST)
        if form.is_valid():
            original_text = form.cleaned_data['original_text']
            number_sentences = form.cleaned_data['number_sentences']
            summarizer = TextRankSummarizer(number_sentences)
            summary = summarizer.summarize(original_text)
            #summary = 'this is a sample summary'
            return render(request, 'index.html', {'summary': summary, 'form': SummaryForm() })
    return render(request, 'index.html', {'form': SummaryForm() })