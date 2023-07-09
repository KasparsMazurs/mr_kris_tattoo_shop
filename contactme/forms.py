from django import forms

class EmailForm(forms.Form):
    """
    Form for capturing email and message inputs.

    The form includes fields for email and message, with appropriate labels
    and widgets for user input.
    """

    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)
    