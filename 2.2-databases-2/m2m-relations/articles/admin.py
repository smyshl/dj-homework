from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):

    def clean(self):
        is_main_list = []
        for form in self.forms:

            print(form.cleaned_data.get('is_main'))
            is_main_list.append(form.cleaned_data.get('is_main'))

        print(is_main_list)
        if len(is_main_list) and not is_main_list.count(True) == 1:
            raise ValidationError('Для статьи должен быть указан основной раздел и он может быть только один')

        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 0
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at']
    inlines = [ScopeInline, ]


@admin.register(Tag)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Scope)
class ArticleAdmin(admin.ModelAdmin):
    pass
