class EmailForm(forms.Form):
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)