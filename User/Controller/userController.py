# Der Benutzer wird aus dem Modell importiert
from User.Model.user import user

# Eine Funktion, um einen neuen Benutzer zu erstellen
def createUser(email, name, password, adresse, tel):
#Ein Benutzerobjekt wird mit den übergebenen Daten erstellt
    createdUser = user(email, name, password, adresse, tel)
    #Erstellter Benutzer wird in die Datenbank gespeichert
    createdUser.speichern()
