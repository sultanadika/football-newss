from django.forms import ModelForm
from .models import News   # relative import

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["title", "content", "category", "thumbnail", "is_featured"]
    