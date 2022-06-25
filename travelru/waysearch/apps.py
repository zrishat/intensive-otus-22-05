"""
apps
"""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WaysearchConfig(AppConfig):
    """
    waysearch
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "waysearch"
    verbose_name = _("waysearch")
