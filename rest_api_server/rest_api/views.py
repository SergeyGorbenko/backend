from rest_framework import mixins, generics

from rest_api.models import Url as UrlModel
from rest_api.serializers import UrlSerializer


class UrlsDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                     generics.RetrieveAPIView):
    """
    get url detail
    """
    permission_classes = []
    authentication_classes = []
    serializer_class = UrlSerializer
    queryset = UrlModel.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        """
        update existing url

        :param request:
        :param args:
        :param kwargs:
        :return: updated url
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        delete current url

        :param request:
        :param args:
        :param kwargs:
        :return: code 204
        """
        return self.destroy(request, *args, **kwargs)


class UrlsAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    """
    get list urls
    """
    permission_classes = []
    authentication_classes = []
    serializer_class = UrlSerializer
    queryset = UrlModel.objects.all()
    passed_id = None

    def post(self, request, *args, **kwargs):
        """
        create new url

        :param request:
        :param args:
        :param kwargs:
        :return: created url
        """
        return self.create(request, *args, **kwargs)

