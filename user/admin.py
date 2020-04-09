from django.contrib import admin

from .models import Profile, AddressRegistration, AddressActual, AddressPost


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Профиль пользователя"""
    list_display = ('id', 'full_name')
    list_display_links = ('full_name',)


@admin.register(AddressRegistration)
class AddressRegistrationAdmin(admin.ModelAdmin):
    """Адрес регистрации"""
    list_display = ('id', 'name')
    list_display_links = ('name',)


@admin.register(AddressActual)
class AddressActualAdmin(admin.ModelAdmin):
    """Адрес фактического проживания"""
    list_display = ('id', 'name')
    list_display_links = ('name',)


@admin.register(AddressPost)
class AddressPostAdmin(admin.ModelAdmin):
    """Почтовый адрес для связи"""
    list_display = ('id', 'name')
    list_display_links = ('name',)
