from django.shortcuts import render
from django.db import OperationalError


# Create your views here.
def index(request):
    """Simple index view kept for compatibility with other code.
    Renders the app's index template.
    """
    return render(request, 'rwJourney/index.html')


def about_me(request):
    """Render an About Me page. If the AboutMe table is missing or empty,
    render the template with a safe default so the site doesn't 500.
    """
    about = None
    try:
        # Import here to avoid circular import at module load time if migrations aren't applied
        from .models import AboutMe
        about = AboutMe.objects.first()
    except OperationalError:
        # Database table doesn't exist yet (migrations not applied)
        about = None

    context = {
        'about': about
    }
    return render(request, 'rwJourney/aboutMe.html', context)


def learning_journey(request):
    """Render a list of learning entries. If the DB isn't ready, show an empty list."""
    entries = []
    try:
        from .models import LearningEntry
        entries = LearningEntry.objects.order_by('-date')
    except OperationalError:
        entries = []

    return render(request, 'rwJourney/index.html', {'entries': entries})


