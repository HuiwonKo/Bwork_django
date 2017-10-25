from django.conf.urls import url

from commutes import views

urlpatterns = [
    url(r'^$', views.CommuteListAPIView.as_view(), name='list'),
    url(r'^user/(?P<user_pk>\d+)/$', views.UserCommuteListAPIView.as_view(), name='user_commute_list'),
    url(r'^create/$', views.CommuteCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+[-]\d+)/$', views.CommuteDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+[-]\d+)/update/$', views.CommuteUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>\d+[-]\d+)/delete/$', views.CommuteDestroyAPIView.as_view(), name='delete')
]