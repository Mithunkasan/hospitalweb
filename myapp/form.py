from django import forms

from myapp.models import Booking


class bookingform(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'