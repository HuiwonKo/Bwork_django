from django.conf.urls import url
from notices import views

urlpatterns = [
    url(r'^$', views.NoticeListAPIView.as_view(), name='list'),
    url(r'^create/$', views.NoticeCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.NoticeDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.NoticeUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.NoticeDestroyAPIView.as_view(), name='delete'),
]