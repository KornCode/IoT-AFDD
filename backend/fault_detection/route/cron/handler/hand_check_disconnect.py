import asyncio
import logging
import threading

from django.http import JsonResponse
from fault_detection.service.serv_cron import publish_event_disconnect_alert

logger = logging.getLogger(__name__)


def publish_disconnect_alert(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    def run_in_background():
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.create_task(publish_event_disconnect_alert())
            loop.run_forever()
        except Exception as e:
            logger.exception("❌ Error in background publishing task")

    threading.Thread(
        target=run_in_background,
        name="DisconnectPublisherThread",
        daemon=True,
    ).start()

    return JsonResponse({"success": True, "message": "Disconnect config publish started in background"})
