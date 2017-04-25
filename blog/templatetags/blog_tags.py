from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
from markdown.extensions.codehilite import CodeHiliteExtension

from ..models import Post

import markdown

register = template.Library()


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


@register.simple_tag(takes_context=True)
def get_like_session(context, post_id):
    request = context['request']
    return request.session.get('liked_{}'.format(post_id))


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text, extensions=[CodeHiliteExtension()]))
