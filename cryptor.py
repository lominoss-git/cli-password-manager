from cryptography.fernet import Fernet

def encrypt_password(key: bytes, password: str):
    encoded_password = password.encode()
    
    f = Fernet(key)
    encoded_encrypted_password = f.encrypt(encoded_password)
    
    decoded_encrypted_password = encoded_encrypted_password.decode()
    return decoded_encrypted_password

def decrypt_password(key: bytes, encrypted_password: str):
    encoded_encrypted_password = encrypted_password.encode()

    f = Fernet(key)
    
    try:
        encoded_decrypted_password = f.decrypt(encoded_encrypted_password)
        
        original_password = encoded_decrypted_password.decode()
        return original_password

    except:
        return ""
    