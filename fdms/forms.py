# viethis is the form to create institutions, beneficary and securities  information
from django import forms
from django.forms import ModelForm
from fdms.models import Institutions, Beneficiary, Securities


# create a form class for institutions
class Instform(forms.Form):
    instype = forms.CharField(label="Institution Type", max_length=30)
    instname = forms.CharField(label="Institution Name", max_length=30)
    instaddr = forms.CharField(label="Inst Address", max_length=100)

    
# create a form for Beneficiary
class BeneficiaryMF(ModelForm):
    class Meta:
        model = Beneficiary
        fields = ['benef_name', 'benef_contact']

        
# create a ModelForm for Institution
class InstitutionMF(ModelForm):
    class Meta:
        model = Institutions
        fields = ('instname', 'instype', 'instaddr')


# create a form field to upload the certificate in file format

class CertUpload(forms.Form):
    title=forms.CharField(max_length=40)
    fileupload=forms.FileField()


    
