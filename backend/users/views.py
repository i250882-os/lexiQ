# views.py
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response

class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh = response.data.pop("refresh")
        response.set_cookie("refresh", refresh, httponly=True, secure=False, samesite="Strict", max_age=7*24*3600)
        return response

class RefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        request.data["refresh"] = request.COOKIES.get("refresh", "")
        return super().post(request, *args, **kwargs)
