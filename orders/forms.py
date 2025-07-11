from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone', 'address', 'city', 'postal_code', 
                  'payment_method', 'delivery_instructions']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'delivery_instructions': forms.Textarea(attrs={'rows': 3}),
        } 