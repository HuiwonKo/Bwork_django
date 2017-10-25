# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings

from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView

from notices.models import Notice
from notices.serializers import NoticeSerializer

from rest_framework.views import exception_handler
from rest_framework import permissions


class NoticeListAPIView(ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

    def get(self, request, *args, **kwargs):
        print("here")
        return self.list(request, *args, **kwargs)

    def custom_exception_handler(exc, context):
        # Call REST framework's default exception handler first,
        # to get the standard error response.
        response = exception_handler(exc, context)

        # Now add the HTTP status code to the response.
        if response is not None:
            response.data['status_code'] = response.status_code

        return response




class NoticeDetailAPIView(RetrieveAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

    def get(self, request, *args, **kwargs):
        print(kwargs)
        return self.retrieve(request, *args, **kwargs)


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



class NoticeCreateAPIView(CreateAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': data[api_settings.URL_FIELD_NAME]}
        except (TypeError, KeyError):
            return {}



class NoticeUpdateAPIView(UpdateAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

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


class NoticeDestroyAPIView(DestroyAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

"""
class CurrentNoticeListAPIView(ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

    @override
    def get_queryset(self):
"""

