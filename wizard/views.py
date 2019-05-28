from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.core.mail import send_mail, BadHeaderError
import json

# Create your views here.
from wizard.models import Question, Destination, Persona, Post
from .forms import NewForm
#from formtools.wizard.views import SessionWizardView


def index(request):

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        print("posted to index: ")
        print(request.POST)

        if request.POST['reset'] == 'True':
            print("resetting")
            request.session['_known']=False
        else:
            request.session['_old_post'] = request.POST
            request.session['_known'] = True
            post = Post.objects.create(post=json.dumps(request.POST))
        return HttpResponseRedirect(reverse('index'))



    else:    
        print("requested index")
        #print("Loading index with old_post:" + str(request.session['_old_post']))
        old_post = request.session.get('_old_post')
        #persona = find_persona(old_post)
        form = NewForm(request.GET)
        num_questions = Question.objects.count() + 2
        box_width = 100/(num_questions)
        progress_width = 100/(num_questions-2)
        if request.session.get('_known') == True:
            print("we know this person")
            persona = find_persona(old_post)
            context = {'destinations' : Destination.objects.filter(persona=persona), 'progress_width': progress_width,'box_width': box_width, 'known': request.session['_known'], 'form': form, 'questions' : Question.objects.all().order_by('-priority'), 'num_questions' : num_questions}

            
        else:
            print("we don't know this person")
            request.session['_known']=False
            persona = None
            context = {'destinations' : Destination.objects.filter(persona=persona), 'progress_width': progress_width,'box_width': box_width, 'known': request.session['_known'], 'form': form, 'questions' : Question.objects.all().order_by('-priority'), 'num_questions' : num_questions}

        
        #request.session['_old_post'] = request.POST
        print("before final render and known is:")
        print(request.session['_known'])
        return render(request, 'index.html', context=context)

# remove this one
def embedded_wizard(request):
    num_questions = Question.objects.count() + 1
    context = {'questions' : Question.objects.all().order_by('-priority'), 'num_questions' : num_questions}
    return render(request, 'embedded_wizard.html', context=context)

# Results page with destinations!
def destinations(request):
#    old_post = request.session.get('_old_post')
#    persona = find_persona(old_post)
    context = {'destinations' : Destination.objects.all() }
    return render(request, 'all_destinations.html', context=context)

def find_persona(old_post):
    # list with answers
    if old_post:
        answers = [v for v in old_post.values()][1:]
        print("here are all answers:")
        for a in answers:
            print(a)


        personas = Persona.objects.all()
        print("these are all personas:")
        
        persona = None
        for p in personas:
            match = None
            selected_persona = None
            #print("Persona name:")
            #print(p)
            answer=""
            for a in p.answer.all():
                #print("Running first answer:")
                #print((str(a.id) + "_" + a.text))
                answer = (str(a.id) + "_" + a.text)
                if answer in answers and match != False:
                    #print("matching one answer")
                    match = True
                    selected_persona = p
                else: 
                    match = False
            print("ending search and match is:")
            print(match)
            print(selected_persona)

            if match:
                persona = p
                #print("we have a true match:")
                #print(p)
                break

        return persona
