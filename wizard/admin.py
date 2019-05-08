from django.contrib import admin

# Register your models here.
from wizard.models import Question, Answer, Destination


admin.site.register(Answer)

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    
    inlines = [AnswerInline]


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):   
    fields = ['name']