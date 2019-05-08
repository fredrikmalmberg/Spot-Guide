from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
from wizard.models import Question, Destination
from .forms import NewForm
#from formtools.wizard.views import SessionWizardView


def index(request):

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        #form = RenewBookForm(request.POST)
        request.session['_old_post'] = request.POST
        print("gotaget")
        print(request.POST)
        print(request.session.get('_old_post'))
        return HttpResponseRedirect(reverse('destinations'))
        # Check if the form is valid:
        #if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
        #    book_instance.due_back = form.cleaned_data['renewal_date']
        #    book_instance.save()

            # redirect to a new URL:
        #    return HttpResponseRedirect(reverse('all-borrowed') )



    else:    
	    form = NewForm(request.GET)
	    num_questions = Question.objects.count() + 1
	    context = {'form': form, 'questions' : Question.objects.all().order_by('-priority'), 'num_questions' : num_questions}
	    request.session['_old_post'] = request.POST

	    return render(request, 'index.html', context=context)

# remove this one
def embedded_wizard(request):
    num_questions = Question.objects.count() + 1
    context = {'questions' : Question.objects.all().order_by('-priority'), 'num_questions' : num_questions}
    return render(request, 'embedded_wizard.html', context=context)

# Results page with destinations!
def destinations(request):
    old_post = request.session.get('_old_post')
    #num_visits = request.session.get('num_visits', 0)
    context = {'destinations' : Destination.objects.all(), 'old_post' : old_post }
    return render(request, 'destinations.html', context=context)
