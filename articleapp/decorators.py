from django.http import HttpResponseForbidden
from articleapp.models import Article

def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        print('pk:',kwargs['pk'])
        article = Article.objects.get(pk=kwargs['pk'])
        print(article.writer)
        print(request.user)
        if not article.writer == request.user:
            print('invalid...')
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated