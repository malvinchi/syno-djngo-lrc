from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from .forms import Instform, BeneficiaryMF, InstitutionMF
from django.views import View
from django.contrib import messages
from .models import Beneficiary


# Create your views here.
# home page rendering
def home(request):
    wlcom = "Welcome to FDMS(Finanacial Deposits) - Home"
    remote = request.META['REMOTE_ADDR']

    try:
        ua = request.META['HTTP_USER_AGENT']

    except KeyError:
        ua = 'unknown'
        
    context = {"wlc" : wlcom, 'title':"FDMS- Home", "remote_addr": remote, "user_agent": ua}

    return render(request, "fdms/welcome.html", context)
#    return HttpResponse("<h2> Welcome to FDMS </h2>")

#def fdms_create_mf(request):
#    if request.method == "POST":
#        form_mf=InstitutionMF(request.POST)
#        if form_mf.is_valid():
#            form_mf.save()
#            return HttpResponseRedirect(request, "thanks/")
#    else:
#        return HttpResponse(request, "fdms/create.html", context)
#            form_mf=InstitutionMF()


def fdms_create_bf(request):
    #benef=BeneficiaryMF()
#    try:
        if request.method == "POST":
            benef = BeneficiaryMF(request.POST)
            if benef.is_valid():
                benef.save()
                return redirect('thanks/')
#                messages.success(request, "Added Info Successful") message is used inside admin app iguess
            else:
                return redirect('error/')
#                messages.error(request, "Enter Valid Data") used inside admin app

        benef = BeneficiaryMF()

        title="CreateMF_Page"
        header="Create  Db Info"
        context={'title':title, 'header':header, "form1":benef} 

        return render(request, 'fdms/create.html', context)

#    except TypeError:
#        return render(request, 'fdms/error.html')



def fdms_thanks(request):
    return render(request, 'fdms/thanks.html')

def fdms_error(request):
    return render(request, 'fdms/error.html')

#CREATING A CLASS BASED VIEW for Heading in each crud page

class GreetingMsg(View):
    greetings="this is a Greeting"

    def get(self, request):
        greetings="Hello , gonna Delete"
        form_mf1=InstitutionMF()
        context={'form21':form_mf1}
        return render(request, 'fdms/delete.html', context)
    
    def post(self, request):
        greetings="Hello, gonna POST Delete"
        return HttpResponse(greetings)
    
def fdms_update(request):
    if request.method == "POST":
        benf2 = BeneficiaryMF(request.POST)
        
        if benf2.is_valid():
            benf2.save()
    else:
        benf21=BeneficiaryMF()

    
    wlcom = "Update your DB"
    context={'form1': benf21, "wlc": wlcom }
    return render(request, "fdms/update.html", context)

def fdms_read(request):
    if request.method == 'POST':
        if request.is_valid():
            pass
    
#    readform=Instform(request)
#    context={'formr1': readform}
    return render(request, 'fdms/read.html')
