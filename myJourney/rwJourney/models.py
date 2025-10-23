from django.db import models

# Create your models here.
# Model to store each learning entry in your journey
class LearningEntry(models.Model):
    # Title of the learning entry
    title = models.CharField(max_length=120)
    
    # Date when the learning entry was created or noted
    date = models.DateField()
    
    # Detailed description of what was learned
    content = models.TextField()

    # String representation of the object in admin interface
    def __str__(self):
        return f"{self.date} - {self.title}"


# Model to store personal information about yourself
class AboutMe(models.Model):
    # Full name of the student
    full_name = models.CharField(max_length=100)
    
    # Roll number (optional)
    roll_number = models.CharField(max_length=30, blank=True)
    
    # Short bio or description about yourself (optional)
    bio = models.TextField(blank=True)
    
    # Email address (optional)
    email = models.EmailField(blank=True)

    # String representation in admin interface
    def __str__(self):
        return self.full_name