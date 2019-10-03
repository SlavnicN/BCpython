#validate_message.py
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def fetch_public_key(user):
    with open(user.decode('ascii') + "key.pub", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend())
    return public_key

#Message coming from user
message = b"Nelson likes cat"
signature = b"\x1a\xafnH\xcdx\xe8\xfa\xcb\xdf\xe9\xbe\x1b\x9d\x8d\x80\x9a; \x8f\xa9\x85{XW\x89%c\x82\xf6\x14\xb1}mi\x05\x8ev\xf6h\xf1\xfe\t9\xdc\x0b\xf2\x11\xb5\x1cmt\x89\xf4\x9e\xa1\xffN\xce\xe3sR\xa91\xc8\xedP5\xad\xdc\x94\x95a4*A\xe5\x94i\x16\x0eS^\xbdZ\xc7iK\xfe\x8b\xea\xd0\x8f\xeeD5\xf8Y\x19\xd4\xb9\xb0D\xa0\x00\xaa\x8b|\xe0'\xef\xf3\x19\x15x\x8b\x8a\xd3\x1cHo\x14\xb9\xf6\x0b\xd5yr"

user = message.split()[0].lower()
#fetch public key from Nelson 
public_key = fetch_public_key(user)

# ... verify the message like before
public_key.verify(
    signature,
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256())
