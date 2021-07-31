from django.conf.urls import include, url
from django.urls import path
from django.views.generic import TemplateView
from django.contrib import admin
from rest_framework import routers,views
from rest_framework.schemas import get_schema_view
from rest_framework_json_api.schemas.openapi import SchemaGenerator
from rest_framework.authtoken.views import obtain_auth_token  
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from protoapi import views

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'record', views.RecordViewSet)
router.register(r'type', views.TypeViewSet)
router.register(r'user', views.UserViewSet)

app_name='protoapi'

urlpatterns = [
    url(r"^protoapi/", include(router.urls)),
    path('protoapi/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('protoapi/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('protoapi/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    url(r'^protoapi/admin/', admin.site.urls),


    path(
        "openapi",
        get_schema_view(
            title="Proto API",
            description="API to parse bytes into relational models",
            version="0.1.0",
            generator_class=SchemaGenerator,
        ),
        name="openapi-schema",
    ),
    path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
]