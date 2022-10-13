from django import forms
from django.forms import ValidationError
from issuetracker.models.issues import Issue
from django.core.validators import MinLengthValidator, BaseValidator



def max_length_validator(string):
    if len(string) > 15:
        raise ValidationError("Максимальная длина строки 15 символов")
    return string


class CustomLengthValidator(BaseValidator):
    def __init__(self, limit_value=20, message=''):
        super(CustomLengthValidator, self).__init__(limit_value=limit_value, message=message)

    def compare(self, value, max_value):
        return max_value < value

    def clean(self, value):
        return len(value)

       

        

class IssueForm(forms.ModelForm):
    title = forms.CharField(
        label='Заголовок',
        validators=(
            MinLengthValidator(limit_value=2), 
            CustomLengthValidator(),
            ),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Issue
        fields = ('title', 'description', 'status', 'type_issue')
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:150px'}),
            'status': forms.RadioSelect,
            'type_issue': forms.CheckboxSelectMultiple
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Issue.objects.filter(title=title).exists():
            raise ValidationError('Заголовок с таким названием уже существует')
        return title


