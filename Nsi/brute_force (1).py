import hashlib
import time

debut = time.time()

def hash_password(password):
    hash = hashlib.sha256()
    hash.update(password.encode('utf-8'))
    return hash.hexdigest()


def brute_force_hash(hashed_password):
    # Liste de caractères possibles dans le mot de passe
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # Longueur maximale du mot de passe
    max_length = 4
    # Parcours de toutes les combinaisons possibles
    for length in range(1, max_length + 1):
        for password in generate_passwords(characters, length):
            #print(password)
            # Hache le mot de passe généré
            hashed = hash_password(password)
            # Vérifie si le hachage correspond au hachage donné
            if hashed == hashed_password:
                return password

def generate_passwords(characters, length):
    # Génère toutes les combinaisons possibles de mots de passe
    if length == 1:
        return characters
    else:
        passwords = []
        for char in characters:
            for password in generate_passwords(characters, length - 1):
                passwords.append(char + password)
        return passwords

# Test

hash_psw = input("Entrez le mot de passe hashé :")

hashed_password = hash_psw
password = brute_force_hash(hashed_password)

end = time.time()

if password:
    print(f"Le mot de passe est : '{password}' trouvé en {end-debut} secondes")
else:
    print("Aucun mot de passe correspondant trouvé.")


