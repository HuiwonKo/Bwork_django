# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView

from commutes.serializers import CommuteSerializer
from commutes.models import Commute
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

class CommuteListAPIView(ListAPIView):
    """
    def get_user_pk(self):
        pk = self.args['pk']
        return pk
    """
    queryset = Commute.objects.all()
    serializer_class = CommuteSerializer
    ordering = ('-created_at',)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



class UserCommuteListAPIView(ListAPIView): # 유저별 최신순 정렬된 commute 목록
    serializer_class = CommuteSerializer

    # Queryset Filtering
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user_pk = self.kwargs['user_pk']
        return Commute.objects.filter(user=user_pk)

    def get(self, request, *args, **kwargs):
        print(kwargs)
        return self.list(request, *args, **kwargs)





class CommuteDetailAPIView(RetrieveAPIView):
    queryset = Commute.objects.all()
    serializer_class = CommuteSerializer

    def get(self, request, *args, **kwargs):
        print(kwargs)
        return self.list(request, *args, **kwargs)



    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_object(self):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj



class CommuteCreateAPIView(CreateAPIView):
    queryset = Commute.objects.all()
    serializer_class = CommuteSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




class CommuteUpdateAPIView(UpdateAPIView):
    queryset = Commute.objects.all()
    serializer_class = CommuteSerializer

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



class CommuteDestroyAPIView(DestroyAPIView):
    queryset = Commute.objects.all()
    serializer_class = CommuteSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
