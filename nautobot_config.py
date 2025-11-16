import os

from nautobot.core.settings import *  # noqa F401,F403
from nautobot.core.settings_funcs import is_truthy, parse_redis_connection

# Add Sub Interface to the InterfaceTypeChoices
from nautobot.dcim.choices import InterfaceTypeChoices

updated_choices = []
for group_name, choices in InterfaceTypeChoices.CHOICES:
    if group_name == "Virtual interfaces":
        choices = choices + (("sub-interface", "Sub Interface"),)
    updated_choices.append((group_name, choices))
InterfaceTypeChoices.CHOICES = tuple(updated_choices)
# ------------------------------------------------------------------

ALLOWED_HOSTS = os.getenv("NAUTOBOT_ALLOWED_HOSTS", "localhost,host.docker.internal").split(",")

DEBUG = is_truthy(os.getenv("NAUTOBOT_DEBUG", "False"))
METRICS_ENABLED = is_truthy(os.getenv("NAUTOBOT_METRICS_ENABLED", "False"))
CACHES = {
    "default": {
        "BACKEND": os.getenv(
            "NAUTOBOT_CACHES_BACKEND",
            "django_prometheus.cache.backends.redis.RedisCache" if METRICS_ENABLED else "django_redis.cache.RedisCache",
        ),
        "LOCATION": parse_redis_connection(redis_database=1),
        "TIMEOUT": 300,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "",
        },
    }
}

DATABASES = {
    "default": {
        "NAME": os.getenv("NAUTOBOT_DB_NAME", "nautobot"),  # Database name
        "USER": os.getenv("NAUTOBOT_DB_USER", "postgres"),  # Database username
        "PASSWORD": os.getenv("NAUTOBOT_DB_PASSWORD", ""),  # Database password
        "HOST": os.getenv("NAUTOBOT_DB_HOST", "localhost"),  # Database server
        "PORT": os.getenv("NAUTOBOT_DB_PORT", "5432"),  # Database port (leave blank for default)
        "CONN_MAX_AGE": int(os.getenv("NAUTOBOT_DB_TIMEOUT", "300")),  # Database timeout
        "ENGINE": os.getenv(
            "NAUTOBOT_DB_ENGINE",
            "django_prometheus.db.backends.postgresql" if METRICS_ENABLED else "django.db.backends.postgresql",
        ),  # Database driver ("mysql" or "postgresql")
    }
}
SECRET_KEY = os.getenv("NAUTOBOT_SECRET_KEY", "5s^t28cn&amp;d@z18(_#9)pj+z=2)0$#n=l2i_d6(@p)=82yq8=9=")

INSTALLATION_METRICS_ENABLED = is_truthy(os.getenv("NAUTOBOT_INSTALLATION_METRICS_ENABLED", "False"))

PLUGINS = ["nautobot_bgp_models", "nautobottil", "nautobotbrm", "nautobot_circuit_maintenance"]
