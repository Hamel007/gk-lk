from django.contrib import messages
from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.views.generic.base import View

from .forms import UpdateAddressRegistrationForm, UpdateAddressActualForm, UserDocumentForm
from .models import *


class Turn(PermissionRequiredMixin, ListView):
    """Очередь"""
    paginate_by = 10
    template_name = "turn/turn_list.html"
    permission_required = "profile.view_profile"

    # login_url = '/profile/'
    # permission_denied_message = "dfdfdfd"

    def get_queryset(self):
        return Profile.objects.all()


# class Pr(DetailView):
#     """Очередь"""
#     template_name = "profile/profil.html"
#     model = Profile


class MembersCollective(PermissionRequiredMixin, ListView):
    """Члены кооператива"""
    paginate_by = 10
    template_name = "turn/members_list.html"
    permission_required = "profile.view_profile"

    def get_queryset(self):
        return Profile.objects.all()


class PartnerCollective(PermissionRequiredMixin, ListView):
    """Пайщики кооператива"""
    paginate_by = 10
    template_name = "turn/partner_list.html"
    permission_required = "profile.view_profile"

    def get_queryset(self):
        return Profile.objects.all()


class Deal(PermissionRequiredMixin, ListView):
    """В процессе сделки"""
    paginate_by = 10
    template_name = "turn/deal_list.html"
    permission_required = "profile.view_profile"

    def get_queryset(self):
        return Profile.objects.all()


class Calculated(PermissionRequiredMixin, ListView):
    """Полностью рассчитанные"""
    paginate_by = 10
    template_name = "turn/calculated_list.html"
    permission_required = "profile.view_profile"

    def get_queryset(self):
        return Profile.objects.all()


class Debtor(PermissionRequiredMixin, ListView):
    """Должники"""
    paginate_by = 10
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
    """Создаем или обновляем адреса"""

    def post(self, request):
        if request.POST.get("submit_one"):
            form_1 = UpdateAddressRegistrationForm(request.POST)
            if form_1.is_valid():
                obj, created = AddressRegistration.objects.update_or_create(
                    reg_name=request.user, defaults={"country": request.POST.get('country'),
                                                     "region": request.POST.get('region'),
                                                     "city": request.POST.get('city'),
                                                     "street": request.POST.get('street'),
                                                     "house": str(request.POST.get('house')),
                                                     "corpus": request.POST.get('corpus'),
                                                     "flat": request.POST.get('flat'),
                                                     "index": request.POST.get('index'),
                                                     })
                messages.success(self.request, f'Изменения сохранены')
                return redirect('/')

        if request.POST.get("submit_two"):
            form_2 = UpdateAddressActualForm(request.POST)
            if form_2.is_valid():
                obj, created = AddressActual.objects.update_or_create(
                    act_name=request.user, defaults={"country": request.POST.get('country'),
                                                     "region": request.POST.get('region'),
                                                     "city": request.POST.get('city'),
                                                     "street": request.POST.get('street'),
                                                     "house": request.POST.get('house'),
                                                     "corpus": request.POST.get('corpus'),
                                                     "flat": request.POST.get('flat'),
                                                     "index": request.POST.get('index'),
                                                     })
                messages.success(self.request, f'Изменения сохранены')
                return redirect('/')


# class ExemplarView(LoginRequiredMixin, ListView):
#     """Экземпляры"""
#     model = ExemplarDocument
#     template_name = "documents/documents-verif.html"
#     context_object_name = 'exemplar_list'
#
#     def get_queryset(self):
#         # if self.request.user.is_superuser:
#         #     return UserDocument.objects.all()
#         return ExemplarDocument.objects.all()


class VerificationDocView(LoginRequiredMixin, ListView):
    """Документы"""
    model = UserDocument
    template_name = "documents/documents-verif.html"
    context_object_name = 'user_doc'

    def get_queryset(self):
        # if self.request.user.is_superuser:
        return UserDocument.objects.all()
        # return UserDocument.objects.filter(partner_id=self.request.user.id)

    # def get_context_data(self, **kwargs):
    #     context = super(PostDetail, self).get_context_data(**kwargs)
    #     context['comments'] = Comment.objects.filter(post=self.object, is_delete=False).order_by('-created_at')
    #     return context


# class VerificationDocCreate(LoginRequiredMixin, CreateView):
    # """Добавление документов пайщиком"""
    #
    # model = UserDocument
    # form_class = UserDocumentForm
    # template_name = "documents/documents-verif.html"
    #
    # def form_valid(self, form):
    #     # a = UserDocument.objects.filter(sample=self.request.)
    #     form.instance.partner_id = self.request.user.id
    #     # form.instance.exemplar_id = self.request.s
    #     print(self.request)
    #     self.success_url = form.instance.get_absolute_url()
    #     form.save()
    #     return super(VerificationDocCreate, self).form_valid(form)


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
    context_object_name = "admin_users_list"


# -? для теста
class AdminAllVerificationView(PermissionRequiredMixin, ListView):
    """Админка верификация пользователей"""
    model = Profile
    template_name = "administrirovanie/admin-verif.html"
    permission_required = "profile.view_profile"
    context_object_name = "verification_list"


# -? для теста
class AdminAllPaymentView(PermissionRequiredMixin, ListView):
    """Админка подтверждение платежей"""
    model = Profile
    template_name = "administrirovanie/admin-podtv.html"
    permission_required = "profile.view_profile"
    context_object_name = "pay_list"


# -? для теста
class AdminAllSupportView(PermissionRequiredMixin, ListView):
    """Админка техподдержка"""
    model = Profile
    template_name = "administrirovanie/admin-support.html"
    permission_required = "profile.view_profile"
