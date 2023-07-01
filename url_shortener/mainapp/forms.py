from django import forms


class LinkForm(forms.Form):
    link = forms.URLField(label='', max_length=300)

    def is_valid(self):
        if super().is_valid():
            if self.cleaned_data['link'].startswith('http://') or self.cleaned_data['link'].startswith('https://'):
                return True



