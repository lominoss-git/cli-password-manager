
def save_password(service: str, encrypted_password: str):
    lowercase_service = service.lower()
    
    txt_file = open("passwords/" + lowercase_service + ".txt", "w")
    txt_file.write(encrypted_password)
    
    txt_file.close()

def load_password(service: str):
    lowercase_service = service.lower()
    
    try:
        txt_file = open("passwords/" + lowercase_service + ".txt", "r")
        
        encrypted_password = txt_file.read()
        txt_file.close()

        return encrypted_password
    except:
        return ""
