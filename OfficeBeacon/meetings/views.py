from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from meetings.models import Meeting,Participant
from meetings.serializers import MeetingSerializer, ParticipantSerializer, Meeting_ParticipantSerializer

from rest_framework.views import exception_handler
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from django.template.defaultfilters import slugify




# Meeting API View

class MeetingListAPIView(ListAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)




class MeetingDetailAPIView(RetrieveAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)




#meeting name으로 meeting instance 리스트 출력
class MeetingNameDetailAPIView(ListAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    meeting_name = ''

    def get_queryset(self):
        self.meeting_name = slugify(self.meeting_name)
        return Meeting.objects.filter(plan=self.meeting_name)

    # override
    def get(self, request, *args, **kwargs):
        self.meeting_name = request.GET.get('plan', '')
        print('get메서드의 plan:' + self.meeting_name)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class MeetingCreateAPIView(CreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    """
    def dispatch(self, request, *args, **kwargs):
        import pdb;
        pdb.set_trace()  # or print debug statements
        super(Participant, self).dispatch(request, *args, **kwargs)
    """

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class MeetingUpdateAPIView(UpdateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class MeetingDestroyAPIView(DestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()



# Participant API View

class ParticipantListAPIView(ListAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



# 특정 meeting_pk에 대한 참석자 instance 리스트
class ParticipantMeetingListAPIView(ListAPIView):
    serializer_class = ParticipantSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        meeting_pk = self.kwargs['meeting_pk']
        print(meeting_pk)
        return Participant.objects.filter(meeting=meeting_pk)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



class ParticipantDetailAPIView(RetrieveAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)



class ParticipantCreateAPIView(CreateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

    def post(self, request, *args, **kwargs):
        print('post method')
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        print('create method')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print(type(serializer.data['user']))
        print(type(serializer.data['meeting']))
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




class ParticipantUpdateAPIView(UpdateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)




class ParticipantDestroyAPIView(DestroyAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()