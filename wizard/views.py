from django.shortcuts import render, HttpResponse

# Create your views here.
from wizard.models import Question
#from .forms import FormStepOne, FormStepTwo
#from formtools.wizard.views import SessionWizardView


def index(request):
    #form_data = []
    #form_data.append({ "question": "What is your level", "answers": ['crap','ok'] })
    #form_data.append({ "question": "When do you want to go", "answers": ['now','later'] })
    #context = {'form_data' : form_data}
    num_questions = Question.objects.count() + 1
    context = {'questions' : Question.objects.all().order_by('-priority'), 'num_questions' : num_questions}
    return render(request, 'index.html', context=context)

# remove this one
def embedded_wizard(request):
    #form_data = []
    #form_data.append({ "question": "What is your level", "answers": ['crap','ok'] })
    #form_data.append({ "question": "When do you want to go", "answers": ['now','later'] })
    #context = {'form_data' : form_data}
    num_questions = Question.objects.count() + 1
    context = {'questions' : Question.objects.all().order_by('-priority'), 'num_questions' : num_questions}
    return render(request, 'embedded_wizard.html', context=context)

# Results page with destinations!
def destinations(request):
    #form_data = []
    #form_data.append({ "question": "What is your level", "answers": ['crap','ok'] })
    #form_data.append({ "question": "When do you want to go", "answers": ['now','later'] })
    #context = {'form_data' : form_data}
    num_questions = Question.objects.count() + 1
    context = {'destinations' : Destination.objects.all() }
    return render(request, 'destination.html', context=context)

#class FormWizardView(SessionWizardView):
#    template_name = "wizard/wizard.html"
#    form_list = [FormStepOne, FormStepTwo]
#    def done(self, form_list, **kwargs):
#        return render(self.request, 'done.html', {
#            'form_data': [form.cleaned_data for form in form_list],
#        })