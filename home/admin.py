from django.contrib import admin
from django import forms
from home.models import Blog

# Register your models here.
class BlogAdminForm(forms.ModelForm):
    

    class Meta:
        model = Blog
        fields = "__all__"

class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm

admin.site.register(Blog, BlogAdmin)