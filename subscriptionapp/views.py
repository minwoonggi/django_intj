from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscriptionapp.models import Subscription


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk':self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk')) # project_pk를 가진 데이터가 없으면 404
        user = self.request.user

        subscription = Subscription.objects.filter(user=user, project=project)

        if subscription.exists():
            # 구독 정보가 있으면 구독 해제
            subscription.delete()
        else:
            # 구독 정보가 없으면 구독
            Subscription(user=user, project=project).save()
        return super(SubscriptionView, self).get(request, *args, **kwargs)

@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscriptionapp/list.html'
    paginate_by = 5

    # Article에서 가지고 오는 정보 변경
    def get_queryset(self):
        projects = Subscription.objects.filter(user=self.request.user).values_list('project') # user의 모든 구독정보
        # values_list : 구독한 모든 project들 list화
        article_list = Article.objects.filter(project__in=projects)
        return article_list



