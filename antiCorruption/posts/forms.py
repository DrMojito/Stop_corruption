from django import forms
from django.core.exceptions import ValidationError

from .models import Posts


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Posts
        fields = ['title', 'slug', 'descriptions', 'photo', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'descriptions': forms.Textarea(attrs={'colors': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 150:
            raise ValidationError('Длина превышает 200 символов')

        return title
