import datetime

from django import forms
from django.core.exceptions import ValidationError
# ugettext_lazy로 자동번역하기하면 얹혀가나? end user의 언어로 번역할 때 이 기능을 사용함.
from django.utils.translation import ugettext_lazy as _

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    # the easist way to validate a single field is to override the method clean_<fieldname>()
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date -renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data
