from django.conf.urls import url
from . import views
from .feeds import LatestPostsFeed

urlpatterns = [
    # post views
    url(r'^$', views.post_list, name='post_list'),
    url(r'^tag/(?P<tag_slug>[-\w]+)$', views.post_list, name='post_list_by_tag'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
    url(r'^feed/$', LatestPostsFeed(), name='post_feed'),
    url(r'^search/$', views.post_search, name='post_search'),
    # previous login view
    # url(r'^login/$', views.user_login, name='login'),

    # login / logout urls
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login',
        name='logout_then_login'),

    # password urls
    url(r'^password-change/$', 'django.contrib.auth.views.password_change',
        name='password_change'),
    url(r'^password-change/done/$', 'django.contrib.auth.views.password_change_done',
        name='password_change_done'),

    # restore password urls
    url(r'^password-reset/$',
        'django.contrib.auth.views.password_reset',
        name='password_reset'),
    url(r'^password-reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^password-reset/complete/$',
        'django.contrib.auth.views.password_reset_complete',
        name='password_reset_complete'),

    # registration
    url(r'^register/$', views.register, name='register'),
]