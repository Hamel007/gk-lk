from django import template

register = template.Library()


@register.filter()
def active(url, request):
    """активные ссылки меню"""
    # print(url)
    # # print(request.get_full_path())
    page_num = request.GET.get('page')
    pagination = f"{url}?page={page_num}"
    if url == request.get_full_path() or pagination == request.get_full_path():
        return True
    else:
        return False