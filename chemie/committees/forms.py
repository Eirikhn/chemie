from django import forms

from .models import Member


class EditCommittees(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'committee',
            'position',
            'user',
        ]