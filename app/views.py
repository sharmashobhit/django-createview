from django.shortcuts import render

# Create your views here.
def SampleView(request):
    return True


### AUTOMATED IMPORT. MOVE THIS TO TOP OF THE FILE###
from django.views.generic.edit import CreateView

class BlahView1(CreateView):
	template_name = 'BlahView1.html'
	success_url = '<success_url>'
	# form_class = <SubstituteYourForm>

class 12BlahView1(CreateView):
	template_name = '12BlahView1.html'
	success_url = '<success_url>'
	# form_class = <SubstituteYourForm>