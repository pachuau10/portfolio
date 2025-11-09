    # home/models.py

from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    meta = models.CharField(max_length=300)
    content = models.TextField()
    
    # This is the correct field for the uploaded image
    thumbnail_img = CloudinaryField('image', folder='thlalak_portfolio/', null=True, blank=True)

    # 1. ADD THIS PROPERTY to match the template variable {{blog.thumbnail_url}}
    @property
    def thumbnail_url(self):
        # Check if the thumbnail_img field has a file/URL and return its public URL
        if self.thumbnail_img and hasattr(self.thumbnail_img, 'url'):
            return self.thumbnail_img.url
        return "" # Return empty string if no image is present
    
    category = models.CharField(max_length=255, default="uncategorized")
    slug = models.CharField(max_length=100)
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title