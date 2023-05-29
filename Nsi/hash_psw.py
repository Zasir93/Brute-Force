# Créé par moinootheen_z, le 22/05/2023 en Python 3.7
import hashlib

def hash_password(password):
    """
    Hasher mot de passe <= 4 char
    """
    assert len(password) <= 4, "Mot de passe trop long"
    hash = hashlib.sha256()
    hash.update(password.encode('utf-8'))
    return hash.hexdigest()

sh = input("pass : ")
print(hash_password(sh))