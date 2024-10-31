from django.db import models
from sorl.thumbnail import ImageField
# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=140, blank=False, null=False)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.text
    
    def formatted_date(self):
        return self.created_at.strftime('%B %d, %Y at %I:%M %p')