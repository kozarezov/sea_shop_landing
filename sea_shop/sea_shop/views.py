from unicodedata import category
from django.shortcuts import get_object_or_404, redirect, render

from contacts.models import Contact
from about.models import About
from catalogs.models import Catalog
from gallery.models import Gallery
from news.models import News

def index(request):
    """Основная страница."""
    contacts = get_object_or_404(Contact, pk=1)
    about = get_object_or_404(About, pk=1)
    freezing = Catalog.objects.filter(category='Замороженная продукция')
    fresh = Catalog.objects.filter(category='Свежие дары моря')
    snack = Catalog.objects.filter(category='Закуски')
    catalogs = {
        'freezing': freezing,
        'fresh': fresh,
        'snack': snack
    }
    galleryes = Gallery.objects.all()
    news = News.objects.all()

    context = {
        'contacts': contacts,
        'about': about,
        'catalogs': catalogs,
        'galleryes': galleryes,
        'news': news,
    }

    template_name = 'index.html'
    return render(request, template_name, context=context)

def error_404_view(request, exception):
    return render(request, 'error/error404.html')

def error_500_view(request):
    return render(request, 'error/error500.html')

def error_403_view(request, exception):
    return render(request, 'error/error403.html')