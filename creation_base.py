import sqlite3
import pandas as pd

# Création de la base de données et connexion
conn = sqlite3.connect('base_de_donnees.db')
cursor = conn.cursor()

cursor.execute("""DROP TABLE client""")
cursor.execute("""DROP TABLE commande""")

# Création de la table client
cursor.execute('''CREATE TABLE client (
    Client_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nom TEXT NOT NULL,
    Prénom TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE,
    Téléphone TEXT,
    Date_Naissance DATE,
    Adresse TEXT,
    Consentement_Marketing BOOLEAN NOT NULL
)''')

# Création de la table commande
cursor.execute('''CREATE TABLE IF NOT EXISTS commande (
    Commande_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date_Commande DATE NOT NULL,
    Montant_Commande REAL NOT NULL,
    Client_ID INTEGER,
    FOREIGN KEY(Client_ID) REFERENCES Client(Client_ID)
)''')


# Importation des fichiers CSV
clients = pd.read_csv('jeu-de-donnees-clients.csv')
commandes = pd.read_csv('jeu-de-donnees-commandes.csv')

# Insertion des données dans la table client
clients.to_sql('client', conn, if_exists='append', index=False)

# Insertion des données dans la table commande
commandes.to_sql('commande', conn, if_exists='append', index=False)

# Validation des modification et arrêt de la connexion
conn.commit()
conn.close()