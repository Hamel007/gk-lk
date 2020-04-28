from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Profile


class Turn(LoginRequiredMixin, ListView):
    """Очередь"""
    paginate_by = 1
    template_name = "turn/turn_list.html"

    def get_queryset(self):
        return Profile.objects.all()


class MembersCollective(LoginRequiredMixin, ListView):
    """Члены кооператива"""
    paginate_by = 1
    template_name = "turn/members_list.html"

    def get_queryset(self):
        return Profile.objects.all()


class PartnerCollective(LoginRequiredMixin, ListView):
    """Пайщики кооператива"""
    paginate_by = 1
    template_name = "turn/partner_list.html"

    def get_queryset(self):
        return Profile.objects.all()


class Deal(LoginRequiredMixin, ListView):
    """В процессе сделки"""
    paginate_by = 1
    template_name = "turn/deal_list.html"

    def get_queryset(self):
        return Profile.objects.all()


class Calculated(LoginRequiredMixin, ListView):
    """Полностью рассчитанные"""
    paginate_by = 1
    template_name = "turn/calculated_list.html"

    def get_queryset(self):
        return Profile.objects.all()


class Debtor(LoginRequiredMixin, ListView):
    """Должники"""
    paginate_by = 1
    template_name = "turn/debtor_list.html"

    def get_queryset(self):
        return Profile.objects.all()


class ProfileView(PermissionRequiredMixin, DetailView):
    """Профиль пользователя"""
    permission_required = "profile.view_profile"
    model = Profile
    template_name = "profile/profil.html"

    def get_object(self, queryset=None):
        obj = get_object_or_404(Profile, user=self.request.user)
        return obj


# -? для теста
class VerificationDocView(LoginRequiredMixin, ListView):
    """Документы"""
    model = Profile
    template_name = "documents/documents-verif.html"


# -? для теста
class PhotoVerificationDocView(LoginRequiredMixin, ListView):
    """Фотоверификация"""
    model = Profile
    template_name = "documents/documents-photo.html"


# -? для теста
class DocView(LoginRequiredMixin, ListView):
    """Документы"""
    model = Profile
    template_name = "documents/documents-docs.html"


# -? для теста
class SampleDocView(LoginRequiredMixin, ListView):
    """Шаблоны и образцы"""
    model = Profile
    template_name = "documents/documents-shablon.html"


# -? для теста
class InstructionView(LoginRequiredMixin, ListView):
    """Инструкции"""
    model = Profile
    template_name = "documents/documents-instructions.html"


# -? для теста
class EntranceFeeView(LoginRequiredMixin, ListView):
    """Вступительный взнос"""
    model = Profile
    template_name = "vznos/vznos-vznos_vstup.html"


# -? для теста
class SharePremiumView(LoginRequiredMixin, ListView):
    """Паевый взнос"""
    model = Profile
    template_name = "vznos/vznos-vznos_paev.html"


# -? для теста
class ConfirmPaymentView(LoginRequiredMixin, ListView):
    """Подтвердить взнос"""
    model = Profile
    template_name = "vznos/vznos-vznos_podtv.html"


# -? для теста
class HistoryPaymentView(LoginRequiredMixin, ListView):
    """История платежей"""
    model = Profile
    template_name = "vznos/vznos-myvznos.html"


# -? для теста
class HierarchyView(LoginRequiredMixin, ListView):
    """Иерархия приглашений"""
    model = Profile
    template_name = "distribution/ierarhiya.html"


# -? для теста
class LinkInvitationView(LoginRequiredMixin, ListView):
    """Ссылки для приглашения"""
    model = Profile
    template_name = "distribution/raspr-links.html"


# -? для теста
class SupportView(LoginRequiredMixin, ListView):
    """Поддержка"""
    model = Profile
    template_name = "pages/support.html"


# -? для теста
class CalculatorView(LoginRequiredMixin, ListView):
    """Калькулятор"""
    model = Profile
    template_name = "pages/calculator.html"