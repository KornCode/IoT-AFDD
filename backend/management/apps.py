import logging

from django.apps import AppConfig
from django.db import connection

logger = logging.getLogger(__name__)


class ManagementConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "management"

    def ready(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1;")
        logger.info("[SUPABASE] ✅ Connection established successfully.")
