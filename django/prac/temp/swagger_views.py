from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import os
import json
from django.http import HttpResponse,JsonResponse

class SwaggerView(APIView):
    """
    modeified account authentication for Rovi
    as they can only open a web page in get request and nothing else
    Therefore we will redirect the request to auth?token_response path (same thing is done by android app)
    """
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            json_file_path = os.path.join(os.path.dirname(__file__), 'trainman.json')
            if request.GET.get('format') == 'json':
                with open(json_file_path, "r") as f:
                    data = json.load(f)
                return Response(data)
            else:
                return Response({"success": False, "error": 'format value required', "data": []})
        except Exception as e:
            return Response({'status':401,"success": False, "error": str(e), "data": []})


