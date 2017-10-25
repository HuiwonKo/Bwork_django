from django.conf.urls import url
from meetings import views

urlpatterns = [

    # Meeting
    url(r'^meeting/$', views.MeetingListAPIView.as_view(), name='meeting_list'), # Meeting 전체 리스트

    url(r'^meeting/create/$', views.MeetingCreateAPIView.as_view(), name='create'),
    url(r'^meeting/(?P<pk>\d+)/$', views.MeetingDetailAPIView.as_view(), name='detail'),
    url(r'^meeting/name/$', views.MeetingNameDetailAPIView.as_view(), name='meeting_name_detail'),
    url(r'^meeting(?P<pk>\d+)/update/$', views.MeetingUpdateAPIView.as_view(), name='update'),
    url(r'^meeting/(?P<pk>\d+)/delete/$', views.MeetingDestroyAPIView.as_view(), name='delete'),

    #Participant
    url(r'^participant/$', views.ParticipantListAPIView.as_view(), name='participant_list'), #Participant 전체 리스트
    url(r'^participant/meeting/(?P<meeting_pk>\d+)/$', views.ParticipantMeetingListAPIView.as_view(), name='participant_meeting_list'), #Participant meeting 별 리스트

    url(r'^participant/create/$', views.ParticipantCreateAPIView.as_view(), name='create'),
    #url(r'^participant/(?P<pk>\d+)/$', views.ParticipantDetailAPIView.as_view(), name='detail'),

    url(r'^participant/(?P<pk>\d+[-]\d+)/$', views.ParticipantDetailAPIView.as_view(), name='detail'),
    url(r'^participant/(?P<pk>\d+[-]\d+)/update/$', views.ParticipantUpdateAPIView.as_view(), name='update'),
    url(r'^participant/(?P<pk>\d+[-]\d+)/delete/$', views.ParticipantDestroyAPIView.as_view(), name='delete'),
]