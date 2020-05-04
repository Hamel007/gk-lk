from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    """Обратная связь"""
    list_display = ('title', 'user', 'date', "processing", "id")
    list_filter = ("title", "date")
    search_fields = ("title",)


admin.site.register(Feedback, FeedbackAdmin)
