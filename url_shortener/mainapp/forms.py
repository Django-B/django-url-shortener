from django import forms


class LinkForm(forms.Form):
    link = forms.URLField(label='', max_length=300)

    def clean_link(self):
        return self.cleaned_data['link']



