from django.conf.urls import include, url
from django.urls import path
from django.views.generic import TemplateView

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
router.register(r'Record', views.RecordViewSet)
router.register(r'Type', views.TypeViewSet)
router.register(r'User', views.UserViewSet)

app_name='protoapi'

urlpatterns = [
    url(r"^protoapi/", include(router.urls)),
    path('protoapi/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('protoapi/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('protoapi/token/verify', TokenVerifyView.as_view(), name='token_verify'),


    path(
        "openapi",
        get_schema_view(
            title="Example API",
            description="API for all things …",
            version="1.0.0",
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

# if settings.DEBUG:
#     import debug_toolbar

#     urlpatterns = [
#         url(r"^__debug__/", include(debug_toolbar.urls)),
#     ] + urlpatterns
