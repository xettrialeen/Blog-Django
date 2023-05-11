from .models import AboutPage


def about_page(request):
    try:
        about_page = AboutPage.objects.all()
    except AboutPage.DoesNotExist:
        about_page = None

    return {'about_page': about_page[0]}
