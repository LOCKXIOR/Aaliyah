from Aaliyah import Aaliyah

# Données : [Surface (m²), Nb de pièces, Distance centre-ville (km)]

donnees_immo = [
    [32, 1, 2], [150, 5, 18], [45, 2, 4], [210, 7, 25], [28, 1, 1],
    [120, 4, 12], [60, 3, 5], [180, 6, 20], [38, 2, 3], [160, 5, 15],
    [35, 1, 2], [140, 5, 16], [50, 2, 4], [220, 8, 28], [25, 1, 1],
    [130, 4, 14], [65, 3, 6], [190, 6, 22], [40, 2, 3], [170, 5, 17],
    [30, 1, 3], [145, 5, 17], [48, 2, 5], [200, 7, 24], [29, 1, 2],
    [125, 4, 13], [58, 3, 4], [175, 6, 19], [36, 2, 2], [155, 5, 16],
    [33, 1, 2], [135, 4, 15], [52, 2, 4], [205, 7, 26], [27, 1, 1],
    [115, 4, 11], [62, 3, 5], [185, 6, 21], [42, 2, 3], [165, 5, 18]
]

categories_immo = [
    "Appartement", "Maison", "Appartement", "Maison", "Appartement",
    "Maison", "Appartement", "Maison", "Appartement", "Maison",
    "Appartement", "Maison", "Appartement", "Maison", "Appartement",
    "Maison", "Appartement", "Maison", "Appartement", "Maison",
    "Appartement", "Maison", "Appartement", "Maison", "Appartement",
    "Maison", "Appartement", "Maison", "Appartement", "Maison",
    "Appartement", "Maison", "Appartement", "Maison", "Appartement",
    "Maison", "Appartement", "Maison", "Appartement", "Maison"
]

if __name__ == "__main__":
    Aaliyah_=Aaliyah("Estimer le type de logement")
    print(Aaliyah_.goal())
    print(Aaliyah_.train(donnees_immo, categories_immo))
    print(Aaliyah_.answer_to([2400, 20, 40]))