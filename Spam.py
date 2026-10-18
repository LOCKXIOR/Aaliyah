from Aaliyah import Aaliyah

# Données : [Ratio mots suspects (0.0 à 1.0), Nb de liens URL, Longueur du message en mots]

donnees_spam = [
    [0.8, 5, 40], [0.0, 0, 150], [0.6, 3, 20], [0.1, 1, 200], [0.9, 8, 15],
    [0.0, 2, 90], [0.7, 4, 35], [0.0, 0, 300], [0.5, 6, 50], [0.0, 1, 120],
    [0.85, 6, 30], [0.0, 0, 180], [0.65, 4, 25], [0.05, 1, 220], [0.95, 7, 10],
    [0.0, 1, 100], [0.75, 5, 45], [0.0, 0, 250], [0.55, 3, 60], [0.0, 1, 140],
    [0.82, 5, 38], [0.0, 0, 160], [0.62, 3, 22], [0.08, 1, 210], [0.88, 9, 12],
    [0.0, 2, 95], [0.72, 4, 32], [0.0, 0, 280], [0.52, 5, 55], [0.0, 1, 130],
    [0.78, 6, 36], [0.0, 0, 170], [0.68, 4, 28], [0.02, 1, 190], [0.92, 8, 14],
    [0.0, 1, 110], [0.76, 5, 42], [0.0, 0, 260], [0.58, 4, 48], [0.0, 1, 125]
]

categories_spam = [
    "Spam", "Normal", "Spam", "Normal", "Spam",
    "Normal", "Spam", "Normal", "Spam", "Normal",
    "Spam", "Normal", "Spam", "Normal", "Spam",
    "Normal", "Spam", "Normal", "Spam", "Normal",
    "Spam", "Normal", "Spam", "Normal", "Spam",
    "Normal", "Spam", "Normal", "Spam", "Normal",
    "Spam", "Normal", "Spam", "Normal", "Spam",
    "Normal", "Spam", "Normal", "Spam", "Normal"
]

if __name__ == "__main__":
    Aaliyah_=Aaliyah("Détection de spam")
    print(Aaliyah_.goal())
    print(Aaliyah_.train(donnees_spam, categories_spam))
    print(Aaliyah_.answer_to([0.0, 0, 18]))