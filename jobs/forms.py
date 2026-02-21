from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model  = JobApplication
        # We exclude 'user' because we set it automatically in the view
        # We exclude timestamps because Django sets them automatically
        fields = [
            'company',
            'role',
            'status',
            'location',
            'job_url',
            'applied_date',
            'interview_date',
            'notes',
        ]
        widgets = {
            # Add Bootstrap 'form-control' class to every input for styling
            'company':        forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Google'}),
            'role':           forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Backend Developer'}),
            'status':         forms.Select(attrs={'class': 'form-select'}),
            'location':       forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Bangalore (optional)'}),
            'job_url':        forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://... (optional)'}),
            'applied_date':   forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'interview_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'notes':          forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Any extra notes...'}),
        }