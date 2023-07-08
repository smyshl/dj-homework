from django.shortcuts import render

from articles.models import Article, Tag, Scope


def articles_list(request):
    template = 'articles/news.html'

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    object_list = Article.objects.all().order_by(ordering)

    for article in object_list:
        print(article)
        print(article.scopes.all())
        for scope in article.scopes.all():
            print(scope, scope.is_main)

    context = {
        'object_list': object_list
    }

    return render(request, template, context)
