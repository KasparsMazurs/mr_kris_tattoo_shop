from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    Custom widget for clearing file inputs.

    This widget extends the ClearableFileInput widget provided by Django
    and customizes the labels and template used for rendering the widget.
    """

    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'custom_widget_templates/custom_clearable_file_input.html'
