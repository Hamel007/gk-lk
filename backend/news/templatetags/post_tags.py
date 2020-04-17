from django import template

from backend.news.models import Post

register = template.Library()


@register.inclusion_tag('news/news-all.html')
def menu_categories():
    """Вывод статей"""
    return {"posts": Post.objects.filter(published=True)}
