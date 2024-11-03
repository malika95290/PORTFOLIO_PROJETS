"""
Cours "Introduction 1" - Exercice "Billetterie"
"""

# Variables
stations = {
    "Meinohama": 1.5,
    "Muromi": 0.8,
    "Fujisaki": 1.1,
    "Nishijin": 1.2,
    "Tojinmachi": 0.8,
    "Ohorikoen (Ohori Park)": 1.1,
    "Akasaka": 0.8,
    "Tenjin": 0.8,
    "Nakasu-Kawabata": 1.0,
    "Gion": 0.7,
    "Hakata": 1.2,
    "Higashi-Hie": 2.1,
    "Fukuokakuko (Airport)": 0.0,
}
stations_names = list(stations.keys())
stations_distances = list(stations.values())
nb_billets_adulte = 0
has_reduit = False

# Introduction
print("           /////// ")
print("         ///       ")
print("  //////////////   ")
print("      ///          ")
print("///////            ")
print("\nBienvenue sur la billetterie du métro municipal de Fukuoka.")

#FONCTIONS 

def choix_ticket_reduit(message):
    #Propose à l'utilisateur s'il souhaite des tickes réduits
    while True :
        reponse = input(message + "(oui ou non) : ")
        if reponse == "oui":
            return True
        elif reponse == "non" :
            return False
        else : 
            print("Saisir oui ou non")

def saisie_user(message):
    #Vérification si le nombre est positif
    while True :
        valeur = int(input(message))
        if valeur < 0 :
            print("Ce que vous avez tapé ne convient pas, retapez une nouvelle valeur")
        else : 
            return valeur

def verifier_station(num_station):
    #Vérifiction du numéro de station sinon on relance
    while True :
        if num_station < 1 or num_station>len(stations):
            num_station = int(input("Ce que vous avez saisi n'est pas correcte, resaisir une valeur : "))
        else : 
            return num_station

def affichage_station(stations):
    print("\nListe des stations : ")
    for index, station in enumerate(stations):
        print(f'{index + 1} : {station}')

def calculer_distance(station_depart, station_arrivee):
    distance_totale = 0
    if station_depart < station_arrivee:
        for i in range(station_depart, station_arrivee):
            distance_totale += stations[stations_names[i]]  # Ajouter la distance entre chaque paire de stations
    else:
        for i in range(station_arrivee, station_depart):
            distance_totale += stations[stations_names[i]]  # Ajouter la distance entre chaque paire de stations
    return distance_totale

def calculer_prix(distance, tarif_plein, tarif_reduit):
    if distance <= 3:
        return "Zone 1", tarif_plein["Zone 1"], tarif_reduit["Zone 1"]
    elif distance <= 7:
        return "Zone 2", tarif_plein["Zone 2"], tarif_reduit["Zone 2"]
    elif distance <= 11:
        return "Zone 3", tarif_plein["Zone 3"], tarif_reduit["Zone 3"]
    else:
        return "Zone 4", tarif_plein["Zone 4"], tarif_reduit["Zone 4"]

# QUESTIONS A L'UTILISATEUR
nb_billets_adulte = saisie_user("Combien de billets adultes souhaitez-vous ? : ")

#Billets réduits
if choix_ticket_reduit("Souhaitez-vous des tickets réduits ? : ") :
    has_reduit = saisie_user("Combien de billets à tarifs réduits souhaitez-vous ? : ")
else :
    has_reduit = 0

affichage_station(stations)
station_depart = verifier_station(int(input("Quelle est la station de départ ? : ")))
station_arrivee = verifier_station(int(input("Quelle est la station d'arrivée ? : ")))

# Choix de la bonne zone tarifaire
distance = calculer_distance(station_depart, station_arrivee)

# Calcul du coût total
tarif_plein = {"Zone 1": 210, "Zone 2": 260, "Zone 3": 300, "Zone 4": 340}
tarif_reduit = {"Zone 1": 110, "Zone 2": 130, "Zone 3": 150, "Zone 4": 170}
zone_tarifaire, prix_unitaire_plein, prix_unitaire_reduit = calculer_prix(distance, tarif_plein, tarif_reduit)
cout_total = nb_billets_adulte * prix_unitaire_plein + has_reduit * prix_unitaire_reduit

# Affichage des détails du voyage et du tarif
print(f"Zone tarifaire : {zone_tarifaire} - {distance} km")
print(f"Prix unitaire adulte : {prix_unitaire_plein} yen")
print(f"Prix unitaire réduit : {prix_unitaire_reduit} yen")
print(f"Nombre de billets adulte : {nb_billets_adulte}")
print(f"Nombre de billets à tarif réduit : {has_reduit}")
print(f"Coût total : {cout_total} yen")

# Affichage de la voie du train à emprunter
if station_depart < station_arrivee :
    print("Vous devez emprunter la voie 1 dans le sens Meinohama > Fukuokfuko")
else :
    print("Vous devez emprunter la voie 2 dans le sens Fukuokfuko > Meinohama")
