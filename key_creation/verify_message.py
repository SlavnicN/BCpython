from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


PRIVATE_KEY_FILE = "nelsonkey.pem"
PUBLIC_KEY_FILE = "nelsonkey.pub"
MESSAGE = b"Nelson likes cat"

# Load private key from pem file
with open(PRIVATE_KEY_FILE, "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )


signature = private_key.sign(
    MESSAGE,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Load public key from file
with open(PUBLIC_KEY_FILE, "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )


#Message validation executed by other people
public_key.verify(
    signature,
    MESSAGE, 
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256())


print(signature)