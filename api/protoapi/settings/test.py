from .dev import *  # noqa
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

ROOT_URLCONF = "protoapi.urls_test"

JSON_API_FORMAT_FIELD_NAMES = "camelize"
JSON_API_FORMAT_TYPES = "camelize"
JSON_API_PLURALIZE_TYPES = True

REST_FRAMEWORK.update(  
    { 
        "PAGE_SIZE": 1,
    }
)
