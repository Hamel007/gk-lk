from django.db import models


class Calculator(models.Model):
    """Класс модели калькулятор"""
    title = models.CharField("Название программы", max_length=100)
    percent_fee = models.PositiveIntegerField("Процент первоначального взноса", null=True)
    percent_mortgage = models.PositiveIntegerField("Процент ипотеки", null=True)

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name = "Программу для членов ЖК"
        verbose_name_plural = "Программы для членов ЖК"


class ParameterCalculator(models.Model):
    """Параметры калькулятора программы"""
    calculator = models.ForeignKey(Calculator, verbose_name="Название программы", on_delete=models.CASCADE)
    range_from = models.PositiveIntegerField("От", null=True)
    range_to = models.PositiveIntegerField("До", null=True)
    entry_fee = models.PositiveIntegerField("Вступительный взнос", null=True)
    monthly_fee = models.PositiveIntegerField("Ежемесячный членский взнос", null=True)
    min_payment = models.PositiveIntegerField("Минимальный платеж", null=True, blank=True)

    def __str__(self):
        return "{}".format("Диапазон")

    class Meta:
        verbose_name = "Диапазон программы"
        verbose_name_plural = "Диапазон программы"