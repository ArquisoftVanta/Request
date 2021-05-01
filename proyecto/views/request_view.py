from proyecto.models.request_model import Request
from proyecto.serializers.request_serializer import RequestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

class RequestList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class RequestU(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    def get_queryset(self):
        id = self.request.GET.get('user')
        return Request.objects.filter(user_id = id)

    serializer_class = RequestSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class RequestActive(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    def get_queryset(self):
        state = self.request.GET.get('active')
        return Request.objects.filter(active = state)

    serializer_class = RequestSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class RequestService(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    def get_queryset(self):
        service = self.request.GET.get('service')
        return Request.objects.filter(service_id = service)

    serializer_class = RequestSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RequestDetail(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):

    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
            a = self.retrieve(request, *args, **kwargs)
            self.destroy(request, *args, **kwargs)
            return a

