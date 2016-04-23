from django import forms
from .models import LockerUser, Locker, Ownership


class ExternalRegisterLocker(forms.Form):
    class Meta:
        model = LockerUser
        fields = [
            "first_name",
            "last_name",
            "username",
        ]

