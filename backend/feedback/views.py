from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

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
