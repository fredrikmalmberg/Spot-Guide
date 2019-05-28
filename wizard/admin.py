from django.contrib import admin

# Register your models here.
from wizard.models import Question, Answer, Destination, Persona, Image, BulletPoint, Post


admin.site.register(Answer)

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

class ImageInline(admin.TabularInline):
    model = Image
    extra = 0

class BulletPointInline(admin.TabularInline):
    model = BulletPoint
    extra = 0

class PersonaInline(admin.TabularInline):
    model = Persona.destination.through
    

#class PersonaInline(admin.TabularInline):
#    model = Persona
#    extra = 0

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    
    inlines = [AnswerInline]


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):   
    model = Destination
    inlines = [
        PersonaInline, ImageInline, BulletPointInline
    ]
#    inlines = [PersonaInline]

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):   
    #model = Persona
    list_display = ('name', 'description', 'display_destination')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post


