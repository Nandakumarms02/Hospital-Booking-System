from django import forms
from home.models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        widgets = {
            'booking_date' : DateInput(),
        }

        labels = {
            'p_name': "Patient Name:",
            'p_phone': "Phone:",
            'p_email': "Email:",
            'doc_name': "Doctor Name:",
            'booking_date': "Booking Date:",
        }