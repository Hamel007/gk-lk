from django import template

from backend.profile.models import Profile

register = template.Library()


@register.inclusion_tag('include/header.html')
def user_header(pk):
    """Вывод пользователей в хедере"""
    return {"user": Profile.objects.filter(user_id=pk)}
