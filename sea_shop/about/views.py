from django.shortcuts import get_object_or_404, render

from about.models import About

def about(request):
    template_name = 'about/about_full.html'
    about = get_object_or_404(About, pk=1)

    context = {
        'about': about,
    }
    return render(request, template_name, context=context)