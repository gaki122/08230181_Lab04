from django.urls import path
from . import views  # Import views from the current app

# Namespace for this app to avoid URL name clashes
app_name = 'rwJourney'

# URL patterns for this app
urlpatterns = [
    # Homepage URL → calls the 'index' view
    path('', views.index, name='index'),
    
    # About Me page URL → calls the 'about_me' view
    path('about/', views.about_me, name='about'),
]