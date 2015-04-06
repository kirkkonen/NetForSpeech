from django.forms import ValidationError
from django.forms.models import BaseInlineFormSet


class RequiredInlineFormSet(BaseInlineFormSet):
    def clean(self):
        """Check that at least one service has been entered."""
        super().clean()
        if any(self.errors):
            return
        if not any(cleaned_data and not cleaned_data.get('DELETE', False)
                   for cleaned_data in self.cleaned_data):
            raise ValidationError('At least one item required.')