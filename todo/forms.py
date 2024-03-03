from django.forms import DateTimeInput, ModelForm, ValidationError
from django.utils import timezone

from todo.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline']
        widgets = {
            'deadline': DateTimeInput(
                attrs={'type': 'datetime-local'},
            )
        }

    def clean_deadline(self):
        deadline = self.cleaned_data['deadline']
        if deadline < timezone.now():
            raise ValidationError('Deadline cannot be in the past')
        return deadline