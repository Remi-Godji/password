import random
import string
import hashlib
import json

PASSWORDS_FILE = "passwords.json"

def generate_random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(8))
    return password

def is_valid_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in string.punctuation for char in password):
        return False
    return True

def encrypt_password(password):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password.encode('utf-8'))
    encrypted_password = sha256_hash.hexdigest()
    return encrypted_password

def load_passwords():
    try:
        with open(PASSWORDS_FILE, 'r') as file:
            data = file.read()
            if data:
                return json.loads(data)
            else:
                return {}
    except FileNotFoundError:
        return {}
    except json.decoder.JSONDecodeError:
        return {}


def save_passwords(passwords):
    with open(PASSWORDS_FILE, 'w') as file:
        json.dump(passwords, file, indent=2)

def add_password():
    username = input("Entrez le nom d'utilisateur : ")
    user_password = input("Entrez le mot de passe : ")

    if is_valid_password(user_password):
        encrypted_password = encrypt_password(user_password)
        passwords = load_passwords()
        passwords[username] = encrypted_password
        save_passwords(passwords)
        print(f"Le mot de passe pour {username} a été ajouté avec succès.")
    else:
        print("Le mot de passe ne respecte pas les exigences de sécurité. Veuillez choisir un nouveau mot de passe.")

def display_passwords():
    passwords = load_passwords()
    if passwords:
        print("Liste des noms d'utilisateur :")
        for username in passwords.keys():
            print(username)
    else:
        print("Aucun mot de passe enregistré.")

def main():
    while True:
        print("\nMenu:")
        print("1. Ajouter un nouveau mot de passe")
        print("2. Afficher les noms d'utilisateur")
        print("3. Quitter")

        choice = input("Choisissez une option (1/2/3) : ")

        if choice == "1":
            add_password()
        elif choice == "2":
            display_passwords()
        elif choice == "3":
            print("Programme terminé.")
            break
        else:
            print("Option non valide. Veuillez choisir à nouveau.")

if __name__ == '__main__':
    main()
