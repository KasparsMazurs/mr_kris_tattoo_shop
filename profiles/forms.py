from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form for editing user profile information.

    This form is used to update the user profile information.
    It is based on the UserProfile model and excludes the 'user' field.
    """
    class Meta:
        """
        Meta class for the UserProfileForm.
        Specifies the metadata options for the form, including the model
        to associate with (UserProfile) and the fields to exclude (user).
        """
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black profile-form-input'
            self.fields[field].label = False
