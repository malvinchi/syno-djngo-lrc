from django.db import models

# Create your models here.

# INSTITUIONS
class Institutions(models.Model):
    INSTITUTIONS=(('CB', "Canara Bank"), ("DB", "DhanBank"), ("FB", "FedBank"))
    INSTYPE=(("BNK", "Bank"), ("FNC", "FinanceCompany"), ("INS", "InsuranceComp"))

    instname = models.CharField(verbose_name="Name of Institution", max_length=20,  choices=INSTITUTIONS)
    instype = models.CharField(verbose_name="Type of Intstitute", max_length=30,  choices=INSTYPE)
    instaddr = models.CharField(verbose_name="Institution Address", max_length=100, help_text="Enter City Name")

    def __str__(self):
        return self.instname + self.instaddr


#BENEFICIARY
class Beneficiary(models.Model):
    benef_name = models.CharField(max_length=30, unique=True)
    benef_contact = models.EmailField(max_length=54, unique=True)

    def __str__(self):
        return self.benef_name


#SECURITIES
class Securities(models.Model):
    sec_choice = models.TextChoices("Security type", "FD MIS SIP INSR")
    sec_type = models.CharField(verbose_name="Security Type", max_length=20,  choices=sec_choice.choices, default='FD')
    status=models.BooleanField(default=True) # True means Open and False Closed
    doc = models.DateField(verbose_name="Date of Commencement")
    tenure = models.IntegerField(verbose_name="Tenure in months",  default=1)
    roi = models.FloatField(verbose_name="rate of int", default=5.0000)
    dd = models.DateField(verbose_name='due date')
    ipp = models.TextChoices("Interest Proceed Payout", "Cumulative Monthly Quarterly Halfyear  Annual")
    doxs=models.FileField(upload_to='uploads/', default='uploads_old/')
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institutions, on_delete=models.CASCADE)

    def __str__(self):
        return self.sec_type
    

