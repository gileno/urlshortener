from django import forms

from .models import Link


class LinkForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LinkForm, self).__init__(*args, **kwargs)
        self.fields['slug'].required = True
        self.fields['slug'].widget.attrs['placeholder'] = 'Optional'

    # Unique constraint doesn't work with Sqlite3
    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if Link.objects.filter(slug=slug).exists():
            raise forms.ValidationError('This slug already exists')
        return slug

    class Meta:
        model = Link
        fields = ['url', 'slug']
