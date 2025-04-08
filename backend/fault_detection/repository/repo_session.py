from typing import Optional

from django.db import transaction
from django.utils import timezone
from fault_detection.models import FaultDetectionConfig, FaultSession


class SessionResult:
    def __init__(self, session: FaultSession, is_new: bool):
        self.session: FaultSession = session
        self.is_new: bool = is_new


def get_active_session(config: FaultDetectionConfig, target_id: str, datapoint: str) -> Optional[FaultSession]:
    return FaultSession.objects.filter(
        config=config,
        target_id=target_id,
        datapoint=datapoint,
        is_active=True,
    ).first()


@transaction.atomic
def get_or_create_session_safe(config: FaultDetectionConfig, target_id: str, datapoint: str) -> SessionResult:
    session = (
        FaultSession.objects.select_for_update()
        .filter(config=config, target_id=target_id, datapoint=datapoint, is_active=True)
        .first()
    )

    if session:
        return SessionResult(session, is_new=False)

    session = FaultSession.objects.create(
        config=config,
        target_type=config.target_type,
        target_id=target_id,
        datapoint=datapoint,
    )
    return SessionResult(session, is_new=True)


@transaction.atomic
def close_session_safe(session: FaultSession) -> FaultSession:
    session = FaultSession.objects.select_for_update().get(id=session.id)
    session.is_active = False
    session.end_time = timezone.now()
    session.save()
    return session
