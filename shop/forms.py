from django import forms
from .widgets import CustomClearableFileInput
from .models import Product


class ProductForm(forms.ModelForm):
    """
    Form for creating/editing a product.

    This form is used for creating or editing a product.
    It is based on the Product model and includes all fields.
    """
    class Meta:
        """
        Meta class for the ProductForm.

        Specifies the metadata options for the form, including the model
        to associate with (Product) and the fields to include (all fields).
        """
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
