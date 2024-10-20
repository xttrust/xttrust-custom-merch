from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'title', 'body']
        widgets = {
            'rating': forms.Select(choices=[(i, str(i)) for i in range(1, 6)]),
            'body': forms.Textarea(attrs={'rows': 4}),
        }
