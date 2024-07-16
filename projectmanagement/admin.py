from django.contrib import admin

from .models import User, Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1  # Number of empty forms to display
    max_num = 4  # Maximum number of answers allowed

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return max(1, self.max_num - obj.answers.count())
        return self.extra


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ('title', 'difficult_level', 'multiple_choices')
    list_filter = ('difficult_level', 'multiple_choices')
    search_fields = ('title', 'difficult_level')


# Register your models here.
admin.site.register(User)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
