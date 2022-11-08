from django import forms

class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    phone = forms.IntegerField()
    address = forms.CharField(max_length=255)
    zipcode = forms.IntegerField()
    stripe_token = forms.CharField(max_length=255)

