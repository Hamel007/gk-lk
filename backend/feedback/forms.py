from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    """Форма обратной связи"""

    class Meta:
        model = Feedback
        fields = ("title", "text", "image")
