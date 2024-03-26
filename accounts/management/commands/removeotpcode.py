from django.core.management.base import BaseCommand
from accounts.models import OptCode
from datetime import datetime, timedelta
import pytz



class Command(BaseCommand):
    """
    Create a command for manage.py 
    which remove expired OtpCodes

    """
    
    help = 'remove expired otp codes'

    def handle(self, *args, **options):
        expired = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=2)
        OptCode.objects.filter(created__lt=expired).delete()
        self.stdout.write('all expired codes delete')
