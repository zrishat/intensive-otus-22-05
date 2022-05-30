from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WaySearchConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "waySearch"
    verbose_name = _("WaySearch")
