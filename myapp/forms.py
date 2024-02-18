from django import forms
from models import Resume

class Resumeform(forms.modelform):
    class Meta:
        model = Resume  
        field = '__all__'
        
