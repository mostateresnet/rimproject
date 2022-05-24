from hashlib import sha256
from django.conf import settings

API_SECRET = getattr(settings, "API_SECRET", 'test_secret_key')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def validate_req_hash(data, key):
    if "hash" in data and data['hash'].lower() == sha256((str(data[key]) + API_SECRET).encode('utf-8')).hexdigest():
        del data['hash']
        return True
    return False