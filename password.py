import json
import hashlib

PASSWORDS_FILE = "passwords.json"

def encrypt_password(password):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password.encode('utf-8'))
    return sha256_hash.hexdigest()

def load_passwords():
    try:
        with open(PASSWORDS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_passwords(passwords):
    with open(PASSWORDS_FILE, 'w') as file:
        json.dump(passwords, file, indent=2)

def add_password():
    username = input("Entrez le nom d'utilisateur : ")
    password = input("Entrez le mot de passe : ")

    passwords = load_passwords()
    passwords[username] = encrypt_password(password)
    save_passwords(passwords)
    print(f"Le mot de passe pour {username} a été ajouté avec succès.")

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
