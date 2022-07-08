from django.shortcuts import render

def index(request):
    """Основная страница."""
    template_name = 'index.html'
    return render(request, template_name)