from kavenegar import *
from django.contrib.auth.mixins import UserPassesTestMixin


def send_otp_code(phone_number, code):
	"""
	Sending Otp Code from Kavenegar 
	For verify the user 
	
	"""


	try:
		api = KavenegarAPI("#")
		params = {
			'sender': '',
			'receptor': phone_number,
			'message': f'your validation code {code}'
		}
		response = api.sms_send(params)
		print(response)
		
	except APIException as e:
		print(e)
	except HTTPException as e:
		print(e)



class AdminRequiredMixin(UserPassesTestMixin):
	def test_func(self):
		return self.request.user.is_authenticated and self.request.user.is_admin