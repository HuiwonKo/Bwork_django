from django.conf.urls import url
from accounts import views as account_views


urlpatterns = [
    url(r'^$', account_views.ProfileListAPIView.as_view(), name='list'),
    url(r'^user/$', account_views.ProfileUserListAPIView.as_view(), name='user_filtered_list'),
    url(r'^api-token-auth/$', account_views.obtain_auth_token),
    url(r'^create/$', account_views.ProfileCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', account_views.ProfileDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', account_views.ProfileUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', account_views.ProfileDeleteAPIView.as_view(), name='delete'),
]