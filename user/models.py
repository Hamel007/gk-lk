from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """Профиль"""

    # Группа пользователя
    #     - кандидат в пайщики
    #     - пайщик
    #     - должник
    #     - распространитель первого уровня
    #     - распространитель второго уровня
    #     - распространитель третьего уровня
    #     - администратор

    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    number_user = models.CharField("Личный номер пользователя", max_length=50)
    surname = models.CharField("Фамилия", max_length=50)
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Отчество", max_length=50)
    phone = models.CharField("Телефон", max_length=20)
    email = models.EmailField("Email", max_length=50)
    passport = models.CharField("Паспорт", max_length=15)
    birthday = models.DateField("Дата рождения")
    citizenship = models.CharField("Гражданство", max_length=25)
    division_code = models.CharField("Код подразделения", max_length=15)
    date_passport = models.DateField("Дата выдачи паспорта")
    inn = models.PositiveIntegerField("ИНН")
    by_passport = models.CharField("Кем выдан", max_length=250)
    profile_region = models.CharField("Регион", max_length=50)
    profile_city = models.CharField("Город", max_length=50)

    date_activation = models.DateTimeField("Дата активации", help_text="Заполняется администратором", null=True, blank=True)
    accumulated_queue = models.PositiveIntegerField("Накопленно для очереди")
    left_queue = models.PositiveIntegerField("Осталось для очереди")
    documents = models.BooleanField("Документы да/нет", default=False)
    number_queue = models.PositiveIntegerField("Номер очереди")
    date_acquisition = models.DateField("Дата покупки объекта")
    date_joined = models.DateTimeField("Дата активации")
    date_repayment = models.DateTimeField("Дата погашения")
    installment_period = models.DateTimeField("Срок рассрочки")
    percent_installment = models.CharField("Процент рассрочки", max_length=15)
    number_score = models.CharField("Номер счета", max_length=15)

    def __str__(self):
        return self.surname + ' ' + self.first_name + ' ' + self.last_name

    def my_property(self):
        """Склеиваем Фамилию Имя Отчество для админ панели"""
        return self.surname + ' ' + self.first_name + ' ' + self.last_name

    my_property.short_description = "ФИО"
    full_name = property(my_property)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


class AbstractAddressModel(models.Model):
    """Абстрактная модель адреса"""
    country = models.CharField("Страна", max_length=50)
    region = models.CharField("Регион", max_length=50)
    city = models.CharField("Город", max_length=50)
    street = models.CharField("Улица", max_length=50)
    house = models.PositiveIntegerField("Дом")
    corpus = models.CharField("Корпус", max_length=50)
    flat = models.PositiveIntegerField("Квартира")
    index = models.PositiveIntegerField("Индекс")

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"
        abstract = True


class AddressRegistration(AbstractAddressModel):
    """Адрес регистрации"""
    name = models.OneToOneField(Profile, verbose_name="Адрес регистрации", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Адрес регистрации"
        verbose_name_plural = "Адреса регистрации"


class AddressActual(AbstractAddressModel):
    """Адрес фактического проживания"""
    name = models.OneToOneField(Profile, verbose_name="Адрес фактического проживания", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Адрес фактического проживания"
        verbose_name_plural = "Адреса фактического проживания"


class AddressPost(AbstractAddressModel):
    """Почтовый адрес для связи"""
    name = models.OneToOneField(Profile, verbose_name="Почтовый адрес для связи", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Почтовый адрес для связи"
        verbose_name_plural = "Почтовые адреса для связи"


# 4.3. Анкета









