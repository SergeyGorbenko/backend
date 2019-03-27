from django.http import JsonResponse
from django.views.generic import View

from api.forms import UrlForm
from api.mixins import CSRFExemptMixin
from api.utils import generate_keywords_list, get_title, check_url


class APIView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"message": "Keywords API works"}, status=200)


class KeywordsGeneratorAPIView(CSRFExemptMixin, View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"message": "Use only POST request"}, status=405)

    def post(self, request, *args, **kwargs):
        form = UrlForm(request.POST)
        if not form.is_valid():
            return JsonResponse({"message": "Invalid data"}, status=400)
        data = {"url": form.clean_url(),
                'keywords': generate_keywords_list(
                    get_title(
                        check_url(form.clean_url())
                    )
                )}
        return JsonResponse(data, status=202)
