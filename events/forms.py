from django import forms
from .models import Event, User

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'event_date']
        widgets = {
            'event_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['display_name', 'email', 'username']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('password_confirmation'):
            raise forms.ValidationError('パスワードが一致しません')
        return cleaned_data

