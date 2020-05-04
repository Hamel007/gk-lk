from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.base import View

from .forms import UpdateAddressRegistration, UpdateAddressFact
from .models import Profile, AddressRegistration


class Turn(PermissionRequiredMixin, ListView):
    """Очередь"""
    paginate_by = 1
    template_name = "turn/turn_list.html"
    permission_required = "profile.view_profile"
    #login_url = '/profile/'
    # permission_denied_message = "dfdfdfd"

    def get_queryset(self):
        return Profile.objects.all()


class MembersCollective(PermissionRequiredMixin, ListView):
    """Члены кооператива"""
    paginate_by = 1
    template_name = "turn/members_list.html"
    permission_required = "profile.view_profile"

    def get_queryset(self):
        return Profile.objects.all()


class PartnerCollective(PermissionRequiredMixin, ListView):
    """Пайщики кооператива"""
    paginate_by = 1
    template_name = "turn/partner_list.html"
    permission_required = "profile.view_profile"

    def get_queryset(self):
        return Profile.objects.all()


class Deal(PermissionRequiredMixin, ListView):
    """В процессе сделки"""
    paginate_by = 1
    template_name = "turn/deal_list.html"
    permission_required = "profile.view_profile"

    def get_queryset(self):
        return Profile.objects.all()


class Calculated(PermissionRequiredMixin, ListView):
    """Полностью рассчитанные"""
    paginate_by = 1
    template_name = "turn/calculated_list.html"
    permission_required = "profile.view_profile"

    def get_queryset(self):
        return Profile.objects.all()


class Debtor(PermissionRequiredMixin, ListView):
    """Должники"""
    paginate_by = 1
    template_name = "turn/debtor_list.html"
    permission_required = "profile.view_profile"

    def get_queryset(self):
        return Profile.objects.all()


class ProfileView(LoginRequiredMixin, DetailView):
    """Профиль пользователя"""
    # permission_required = "profile.view_profile"
    model = Profile
    template_name = "profile/profil.html"
    # login_url = 'profile'

    def get_object(self, queryset=None):
        obj = get_object_or_404(Profile, user=self.request.user)
        return obj


class CreateAddress(View):
    def post(self, request):
        print(request.POST)
        AddressRegistration.objects.update_or_create(id=request.user.id, street=request.POST.get("street"))
        return HttpResponse(status=201)


# def edit(request):
#     if request.method == 'POST':
#         registration_form = UpdateAddressRegistration(request.POST, instance=request.user.profile.addressregistration)
#         actual_form = UpdateAddressFact(request.POST, instance=request.user.profile.addressactual)
#         if registration_form.is_valid() and actual_form.is_valid():
#             registration_form.save()
#             actual_form.save()
#             return redirect('profile')
#     else:
#         registration_form = UpdateAddressRegistration(instance=request.user.profile.addressregistration)
#         actual_form = UpdateAddressFact()
#         return render(request, 'profile/profil.html', {'registration_form': registration_form, 'actual_form': actual_form})



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
class EntranceFeeView(PermissionRequiredMixin, ListView):
    """Вступительный взнос"""
    model = Profile
    template_name = "vznos/vznos-vznos_vstup.html"
    permission_required = "profile.view_profile"


# -? для теста
class SharePremiumView(PermissionRequiredMixin, ListView):
    """Паевый взнос"""
    model = Profile
    template_name = "vznos/vznos-vznos_paev.html"
    permission_required = "profile.view_profile"


# -? для теста
class ConfirmPaymentView(PermissionRequiredMixin, ListView):
    """Подтвердить взнос"""
    model = Profile
    template_name = "vznos/vznos-vznos_podtv.html"
    permission_required = "profile.view_profile"


# -? для теста
class HistoryPaymentView(PermissionRequiredMixin, ListView):
    """История платежей"""
    model = Profile
    template_name = "vznos/vznos-myvznos.html"
    permission_required = "profile.view_profile"


# -? для теста
class HierarchyView(PermissionRequiredMixin, ListView):
    """Иерархия приглашений"""
    model = Profile
    template_name = "distribution/ierarhiya.html"
    permission_required = "profile.view_profile"


# -? для теста
class LinkInvitationView(PermissionRequiredMixin, ListView):
    """Ссылки для приглашения"""
    model = Profile
    template_name = "distribution/raspr-links.html"
    permission_required = "profile.view_profile"


# -? для теста
class SupportView(LoginRequiredMixin, ListView):
    """Поддержка"""
    model = Profile
    template_name = "pages/support.html"


# -? для теста
class AdminAllUserView(PermissionRequiredMixin, ListView):
    """Админка все пользователи"""
    model = Profile
    template_name = "administrirovanie/admin-allusers.html"
    permission_required = "profile.view_profile"


# -? для теста
class AdminAllVerificationView(PermissionRequiredMixin, ListView):
    """Админка верификация пользователей"""
    model = Profile
    template_name = "administrirovanie/admin-verif.html"
    permission_required = "profile.view_profile"


# -? для теста
class AdminAllPaymentView(PermissionRequiredMixin, ListView):
    """Админка подтверждение платежей"""
    model = Profile
    template_name = "administrirovanie/admin-podtv.html"
    permission_required = "profile.view_profile"


# -? для теста
class AdminAllSupportView(PermissionRequiredMixin, ListView):
    """Админка техподдержка"""
    model = Profile
    template_name = "administrirovanie/admin-support.html"
    permission_required = "profile.view_profile"

