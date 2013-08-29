from django import forms

from models import ContactInfo
from widgets import DateTimeWidget


class ContactInfoForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea)
    other = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField(label='Photo', required=False,
                             error_messages={'invalid': "Image files only"},
                             widget=forms.FileInput)
    birthdate = forms.DateTimeField(
                        widget=DateTimeWidget(attrs={'autoclose': 'true'}))

    class Meta:
        model = ContactInfo
        fields = ("name", "surname", "birthdate", "photo", "email", "jabber",
                  "skype", "other", "bio")
