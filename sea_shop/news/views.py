from django.shortcuts import get_object_or_404, render

from news.models import News

def news(request, pk):
    template_name = 'news/news_full.html'
    news = get_object_or_404(News, pk=pk)

    context = {
        'news': news,
    }
    return render(request, template_name, context=context)