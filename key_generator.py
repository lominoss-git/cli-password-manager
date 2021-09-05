import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

salt = b'\x00V\xd3\xfb\x92\xf3\xdb\xa9vB\xc4\xe1i\xfb\xeb\x93'

def generate_key(master_password: str):
    master_password = master_password.encode()
    
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = 32,
        salt = salt,
        iterations = 100000,
        backend = default_backend()
    )
    
    key = base64.urlsafe_b64encode(kdf.derive(master_password))
    return key
