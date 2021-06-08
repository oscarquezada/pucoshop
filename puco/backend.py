from django.contrib.auth.backends import BaseBackend
from .models import Cliente

class MyBackend(BaseBackend):
    def authenticate(self, request,username=None, password=None):
        try:
            cliente= Cliente.objects.filter(nikename=username, password= password).get()
            return cliente
        except:
            return None
    def get_user(self, user_id) :
        try:
            return Cliente.objects.get(pk=user_id)
        except Cliente.DoesNotExist:
            return None        