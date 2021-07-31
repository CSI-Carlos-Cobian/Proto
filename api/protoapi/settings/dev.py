import os,datetime

SITE_ID = 1
DEBUG = True

MEDIA_ROOT = os.path.normcase(os.path.dirname(os.path.abspath(__file__)))
MEDIA_URL = "/media/"

LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'

CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = (
#     "https://localhost:8000",
#     "https://127.0.0.1:8000",
# )

ALLOWED_HOSTS = [   "localhost",
                    "127.0.0.1", ]


# hiddenimports=[ "django.contrib.admin.apps", 
#                 "django.contrib.auth.apps", 
#                 "django.contrib.contenttypes.apps", 
#                 "django.contrib.sessions.apps", 
#                 "django.contrib.messages.apps", 
#                 "django.contrib.staticfiles.apps", 
#                 "django.contrib.messages.middleware", 
#                 "django.contrib.sessions.middleware", 
#                 "django.contrib.sessions.serializers", 
#                 "django.template.loaders", 
#                 "django.contrib.auth.context_processors", 
#                 "django.contrib.messages.context_processors"]

DATABASE_ENGINE = "mysql"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql", 
        "NAME": "protoapi_db",
        "USER": "protoapi",
        "PASSWORD": "4dHocHomeworkPr0t0",
        "HOST": "127.0.0.1",   # Or an IP Address that your DB is hosted on
        "PORT": "3306",
    }
}

INSTALLED_APPS = [
    "django_extensions",
    "django.contrib.sites",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_swagger",
    "rest_framework.authtoken",
    "rest_framework_json_api",
    "django_filters",
    "corsheaders",
    "drf_generators",
    "factory_generator",
    "polymorphic",
    "protoapi",
    
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # insert your TEMPLATE_DIRS here
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

STATIC_URL = "/static/"

ROOT_URLCONF = "protoapi.urls"

SECRET_KEY = "4dHocHomeworkPr0t0"

PASSWORD_HASHERS = ("django.contrib.auth.hashers.UnsaltedMD5PasswordHasher",)

MIDDLEWARE = (  "corsheaders.middleware.CorsMiddleware",
                "django.contrib.sessions.middleware.SessionMiddleware", 
                "django.middleware.csrf.CsrfViewMiddleware",
                "django.contrib.auth.middleware.AuthenticationMiddleware",
                "django.contrib.messages.middleware.MessageMiddleware",
                "django.middleware.clickjacking.XFrameOptionsMiddleware",
                )

INTERNAL_IPS = ("127.0.0.1",)

JSON_API_FORMAT_FIELD_NAMES = "camelize"
JSON_API_FORMAT_TYPES = "camelize"
REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "rest_framework_json_api.exceptions.exception_handler",
    "DEFAULT_PAGINATION_CLASS": 
        "rest_framework_json_api.pagination.JsonApiPageNumberPagination",
        # "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 16,
    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework_json_api.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ),
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework_json_api.renderers.JSONRenderer",
        # If you're performance testing, you will want to use the browseable API
        # without forms, as the forms can generate their own queries.
        # If performance testing, enable:
        # 'protoapi.utils.BrowsableAPIRendererWithoutForms',
        # Otherwise, to play around with the browseable API, enable:
        "rest_framework_json_api.renderers.BrowsableAPIRenderer",
    ),
    "DEFAULT_METADATA_CLASS": "rest_framework_json_api.metadata.JSONAPIMetadata",
    "DEFAULT_SCHEMA_CLASS": "rest_framework_json_api.schemas.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": (
        "rest_framework_json_api.filters.QueryParameterValidationFilter",
        "rest_framework_json_api.filters.OrderingFilter",
        "rest_framework_json_api.django_filters.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
    ),
    "SEARCH_PARAM": "filter[search]",
    "TEST_REQUEST_RENDERER_CLASSES": (
        "rest_framework_json_api.renderers.JSONRenderer",
    ),
    # "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # "rest_framework.authentication.TokenAuthentication",  # <-- And here
        # "rest_framework.authentication.SessionAuthentication",  # <-- And here
        "rest_framework_simplejwt.authentication.JWTAuthentication",  # <-- And here
        "rest_framework_simplejwt.authentication.JWTTokenUserAuthentication",  # <-- And here
    ],
    "TEST_REQUEST_DEFAULT_FORMAT": "vnd.api+json",
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(minutes=120),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(hours=12),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": SECRET_KEY,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": datetime.timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": datetime.timedelta(days=1),
}


SWAGGER_SETTINGS = {
    "SHOW_REQUEST_HEADERS": True,
    "SECURITY_DEFINITIONS": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    },
    "USE_SESSION_AUTH": True,
    "JSON_EDITOR": True,
    "SUPPORTED_SUBMIT_METHODS": [
        "get",
        "post",
        "put",
        "delete",
        "patch"
    ],
}