from django.contrib import admin

# Register your models here.
from backend.calculator.models import Calculator, ParameterCalculator


class ParameterCalculatorAdmin(admin.TabularInline):
    model = ParameterCalculator


class CalculatorAdmin(admin.ModelAdmin):
    inlines = [ParameterCalculatorAdmin]

    class Meta:
        model = Calculator

admin.site.register(Calculator, CalculatorAdmin)

