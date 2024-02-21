from django import forms
from .models import Resume

GENDER_CHOICES = [
    ('Male','Male'),
    ('Female','Female')
]

JOB_CITY_CHOICES = [

('Banglore','Banglore'),
('Delhi','Delhi'),
('Bombay','Bombay'),
('Noida','Noida'),
('Patna','Patna')

]


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect) # type: ignore
    job_city = forms.MultipleChoiceField(label='Preferred Job Locations',choices = JOB_CITY_CHOICES ,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume  
        fields = ['name','dob','gender','locality','pin','state','mobile','email','job_city','profile_image','my_file']
        
        labels = {
            
                  'name': 'FullName',
                  'dob': 'Date of Birth',
                  'pin': 'Pin Code',
                  'mobile':'Mobile No',
                  'email':'Email Id',
                  'profile_image':'Profile Image',
                  'my_file':'Document'

                  }
        
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob' :forms.DateInput(attrs={'class':'form-control' ,'id':'datepicker'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            #'job_city':forms.Input(attrs={'class':'form-control'})
                
        }
