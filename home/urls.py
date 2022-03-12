from django.conf.urls import url
from home.views import HomeView
from . import views

urlpatterns=[
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_students, name='change_students'),
    url(r'^send_mail_to_fa$', views.send_mail_to_fa, name='send_mail_to_fa'),           ##remove to get the old back.
    url(r'^bonafied-certificate$', views.upload_bonafied_form, name='upload_bonafied_form'),
    url(r'^Internship$', views.Internship, name='Internship'),
    url(r'^Internship/upload$', views.upload_internship_form, name='upload_internship_form'),
    url(r'^onlyforhod$', views.onlyforhod_view, name='onlyforhod'),
    #url(r'^Retest$', views.Retest, name='Retest'),
    url(r'^Retest/upload$', views.upload_retest_form, name='upload_retest_form'),
    url(r'^Retest/retest_list$', views.retest_list, name='retest_list'),
    url(r'^Retest/accepted_students_list$', views.accepted_students_view, name='accepted_students'),
    url(r'^genetate_pdfs$', views.generate_pdfs_view, name='generate_pdfs'),
    url(r'^genetate_pdfs_actual$', views.generate_pdfs_actual, name='generate_pdfs_actual'),
    #url(r'^genetate_obj_pdf$', views.generate_obj_pdf, name='generate_obj_pdf')
]
