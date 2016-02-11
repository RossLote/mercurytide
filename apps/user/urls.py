from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views, forms

urlpatterns = [
    url(r'^password-reset-complete/$',
        auth_views.password_reset_complete,
        {'template_name': 'customer/password/reset-complete.html'},
        name='password_reset_complete'),

    url(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {'template_name': 'customer/password/reset-confirm.html'},
        name='password_reset_confirm'),

    url(r'^password-reset-done/$',
        auth_views.password_reset_done,
        {'template_name': 'customer/password/reset-done.html'},
        name='password_reset_done'),

    url(r'^password-reset/$',
        auth_views.password_reset,
        {'template_name': 'customer/password/reset.html'},
        name="password_reset"),
    url(r'^login/$', auth_views.login,
        {
            'template_name': 'user/login.html',
            'authentication_form': forms.EmailAuthenticationForm
        }, name='login'),
    url(r'^logout/$', auth_views.logout,
        {'next_page': '/'}, name='logout'),
    url(r'^signup/$', views.SignUp.as_view(), name='signup')
]