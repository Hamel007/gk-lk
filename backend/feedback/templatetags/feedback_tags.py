# from django import template
#
# from backend.feedback.models import Feedback
#
# register = template.Library()
#
#
# @register.inclusion_tag('include/feedback_tag.html')
# def feedback_list(count):
#     """Вывод списка обратных связей"""
#     return {"relations": Feedback.objects.all()[:count]}
