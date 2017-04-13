from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

from ..models import Post

@register.simple_tag
def total_posts():
    return Post.published.count()

@register.assignment_tag
def show_latest_posts(count=3):
    return Post.published.order_by('-publish')[:count]

@register.assignment_tag
def get_most_commented_posts(count=3):
    return Post.published.annotate(total_comments=Count('comments')
                                   ).order_by('-total_comments')[:count]

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))