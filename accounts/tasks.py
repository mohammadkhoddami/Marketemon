from celery import shared_task
from .models import OptCode
from datetime import datetime, timedelta
import pytz

@shared_task
def remove_otp_code():
    expired = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=2)
    OptCode.objects.filter(created__lt=expired).delete()