from django import forms

class MakePaymentsForm(forms.Form):

    MONTH_CHOICES = [(i,i) for i in xrange(1,12)]
    YEAR_CHOICES = [(i, i) for i in xrange(2017,2040)]

    credit_card_number = forms.CharField(label='Credit car number')
    cvv = forms.CharField(label='Security code (cvv)')
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label="year", choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

