from django.conf.urls import  url
from accounts import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete


urlpatterns=[
    url(r'^login/$', login, { 'template_name': 'accounts/login.html' }, name='login'),
    url(r'^logout/$', logout, { 'template_name': 'accounts/logout.html'}, name='logout'),
    ##url(r'^register/$', views.register, name='register'),  ##uncomment it to get back to old.
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    url(r'^profile/edit$', views.edit_profile, name='edit_profile'),
    url(r'^change-password$', views.change_password, name='change_passwords'),

    url(r'^reset-password/$', password_reset, { 'template_name': 'accounts/reset_password.html', 'post_reset_redirect':'accounts:password_reset_done',
    'email_template_name':'accounts/reset_password_email.html' }, name='reset_password'),

    url(r'^reset_password/done$', password_reset_done, {'template_name':'accounts/reset-password_reset_done'}, name='password_reset_done'),

    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name':'accounts/reset-password_reset_confirm.html',
        'post_reset_redirect':'password_reset_complete'}, name='password_reset_confirm'),

    url(r'^reset-password/complete/$', password_reset_complete, {'template_name':'accounts/reset-password_reset_complete.html'}, name='password_reset_complete'),

    url(r'^password/$', views.change_password),

    ##
    url(r'^register/$', views.SignUpView.as_view(), name='register'),
    url(r'^register/student/$', views.register, name='student_register'),
    url(r'^register/teacher/$', views.Teacherregister, name='teacher_register'),
    url(r'^register/HOD/$', views.hodregister, name='hod_register'),
    ## remove all if you want to go back to old
]
