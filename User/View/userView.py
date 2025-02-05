# Holt die Funktion zum erstellen eine Benutzers
from User.Controller.userController import createUser

# ein Funktion, um Bentzerdaten vom Nutzer zu bekommen
def getUserData():
    email = input("Deine Email: ")
    name = input("Dein Name: ")
    password = input("Dein Passwort: ")
    adresse = input("Deine Adresse: ")
    tel = input("Deine Telefonnummer: ")

   # Erstellt den Benutzer mit angegebenen Daten
    createUser(email, name, password, adresse, tel)

