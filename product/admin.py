from django.contrib import admin
from .models import Question,Choice



class QuestionAdmin(admin.ModelAdmin):
            #--: simple date and text:--
    # fields = ['pub_date','question_text']
            #--: modify date and text:--
    # fieldsets = [
    #     (None ,             {"fields":["question_text"]}),
    #     ("Date information",{"fields":["pub_date"]}),
    # ]
            #--:add date published:--
    # list_display = ('question_text', 'pub_date')
            ##--:add date published and was_published_recently:--
    
    list_display = ('question_text', 'pub_date', 'was_published_recently')
admin.site.register(Question,QuestionAdmin)

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {"fields":["question_text"]}),
        ("Date information",{"fields":["pub_date"],"classes":["collapse"]}),
    ]
    inlines = [ChoiceInline]
admin.site.register(Choice)



