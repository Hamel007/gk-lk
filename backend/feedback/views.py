from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView

from .models import Feedback
from .forms import FeedbackForm


class FeedbackList(LoginRequiredMixin, ListView):
    """Список обратных связей"""
    paginate_by = 6
    template_name = "feedback/feedback_list.html"

    def get_queryset(self):
        return Feedback.objects.all()


class FeedbackAdminList(LoginRequiredMixin, ListView):
    """Список обратных связей"""
    paginate_by = 6
    template_name = "administrirovanie/admin-support.html"

    def get_queryset(self):
        return Feedback.objects.all()


class FeedbackDetail(LoginRequiredMixin, DetailView):
    """Запрос одного пользователя"""
    model = Feedback
    # template_name = 'feedback/support_detail.html'
    context_object_name = 'single_support'

    def get_queryset(self):
        return Feedback.objects.filter(user_id=self.kwargs.get('pk'))


class FeedbackCreate(LoginRequiredMixin, CreateView):
    """Добавление обратной связи"""
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback_list.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.success_url = form.instance.get_absolute_url()
        form.save()
        message = 'Отправлено в службу поддержки.'
        messages.success(self.request, message)
        return super(FeedbackCreate, self).form_valid(form)
