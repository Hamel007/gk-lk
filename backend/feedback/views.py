from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView, DetailView, View

from backend.profile.models import Profile
from .models import Feedback
from .forms import FeedbackForm


class FeedbackList(LoginRequiredMixin, ListView):
    """Список обратных связей"""
    paginate_by = 6
    template_name = "feedback/feedback_list.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Feedback.objects.all()
        return Feedback.objects.filter(user=self.request.user)


class FeedbackAdminList(LoginRequiredMixin, ListView):
    """Список обратных связей в адменистрированнии"""
    paginate_by = 6
    template_name = "administrirovanie/admin-support.html"

    def get_queryset(self):
        return Feedback.objects.all()

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     return Feedback.objects.filter(user__username=self.request.GET.get('qus'))


class FeedbackDetail(LoginRequiredMixin, DetailView):
    """Детально о запросе"""
    model = Feedback
    context_object_name = 'single_support'

    def get_object(self, queryset=None):
        obj = get_object_or_404(Feedback, id=self.kwargs.get('pk'))
        return obj


# class SearchFeedback(LoginRequiredMixin, ListView):
#     """Поиск пользователей по ФИО"""
#     paginate_by = 5
#     template_name = "administrirovanie/admin-support.html"
#
#     def get_queryset(self):
#         return Feedback.objects.filter(user__username=self.request.GET.get('qus'))


class SearchFeedback(LoginRequiredMixin, View):
    """Поиск пользователей по ФИО"""
    def get(self, request):
        all_users = {'admin_users_list': Profile.objects.filter(full_name=self.request.GET.get('all'))}
        verification = {'verification_list': Profile.objects.filter(full_name=self.request.GET.get('wait'))}
        paying = {'pay_list': Profile.objects.filter(full_name=self.request.GET.get('pay'))}
        support = {'object_list': Feedback.objects.filter(user__username=self.request.GET.get('qus'))}
        if self.request.GET.get('all'):
            return render(self.request, 'administrirovanie/admin-allusers.html', all_users)
        elif self.request.GET.get('wait'):
            return render(self.request, 'administrirovanie/admin-verif.html', verification)
        elif self.request.GET.get('pay'):
            return render(self.request, 'administrirovanie/admin-podtv.html', paying)
        elif self.request.GET.get('qus'):
            return render(self.request, 'administrirovanie/admin-support.html', support)


class FeedbackCreate(LoginRequiredMixin, CreateView):
    """Добавление обратной связи"""
    model = Feedback
    form_class = FeedbackForm
    # template_name = 'feedback/feedback_list.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        # self.success_url = form.instance.get_absolute_url()
        # form.save()
        message = 'Отправлено в службу поддержки.'
        messages.success(self.request, message)
        return super(FeedbackCreate, self).form_valid(form)
