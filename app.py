import argparse
import getpass
import password_generator
import key_generator
import cryptor
import storer
import clipboard

parser = argparse.ArgumentParser()

parser.add_argument("-n", "--new", help="Generate a new random password, copies it to clipboard and stores it in an encrypted form", type=str)
parser.add_argument("-c", "--copy", help="Loads the wanted password and copies it to clipboard", type=str)
parser.add_argument("-s", "--show", help="Loads the wanted password and prints it", type=str)

args = parser.parse_args()

if args.new:
    master_password = getpass.getpass(prompt = "Master Password: ")
    
    password = password_generator.generate_password()
    print(password)
    clipboard.copy(password)
    
    encryption_key = key_generator.generate_key(master_password)
    
    encrypted_password = cryptor.encrypt_password(encryption_key, password)
    
    storer.save_password(args.new, encrypted_password)
    
if args.copy or args.show:
    master_password = getpass.getpass(prompt = "Master Password: ")

    if args.copy:
        encrypted_password = storer.load_password(args.copy)
        
    else:
        encrypted_password = storer.load_password(args.show)
    
    if encrypted_password != "":
        encryption_key = key_generator.generate_key(master_password)
        
        decrypted_password = cryptor.decrypt_password(encryption_key, encrypted_password)
        
        if decrypted_password != "":
            if args.copy:
                clipboard.copy(decrypted_password)
                
            elif args.show:
                print(decrypted_password)
                
        else:
            print("Incorrect master password.")
            
    else:
        print("Password not found.")
