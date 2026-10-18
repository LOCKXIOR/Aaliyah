from Aaliyah import Aaliyah

# Données : [Glycémie (mg/dL), Tension (mmHg), Âge]

donnees_sante = [
    [85, 70, 22], [180, 90, 55], [95, 65, 30], [210, 95, 62], [88, 72, 25],
    [160, 85, 48], [102, 78, 35], [195, 88, 58], [90, 68, 28], [170, 92, 51],
    [110, 75, 42], [145, 80, 60], [82, 60, 20], [220, 100, 65], [105, 70, 38],
    [150, 82, 50], [92, 66, 29], [175, 90, 53], [89, 70, 24], [200, 94, 61],
    [118, 80, 45], [130, 85, 52], [78, 62, 19], [230, 105, 70], [98, 72, 33],
    [165, 88, 56], [91, 64, 27], [185, 92, 59], [86, 68, 23], [172, 86, 49],
    [125, 82, 47], [140, 84, 57], [84, 65, 21], [215, 98, 66], [100, 74, 36],
    [158, 86, 54], [94, 68, 31], [190, 90, 57], [87, 70, 26], [168, 88, 50]
]

categories_sante = [
    "Sain", "Diabétique", "Sain", "Diabétique", "Sain",
    "Diabétique", "Sain", "Diabétique", "Sain", "Diabétique",
    "Sain", "Diabétique", "Sain", "Diabétique", "Sain",
    "Diabétique", "Sain", "Diabétique", "Sain", "Diabétique",
    "Sain", "Diabétique", "Sain", "Diabétique", "Sain",
    "Diabétique", "Sain", "Diabétique", "Sain", "Diabétique",
    "Sain", "Diabétique", "Sain", "Diabétique", "Sain",
    "Diabétique", "Sain", "Diabétique", "Sain", "Diabétique"
]

if __name__ == "__main__":
    Aaliyah_=Aaliyah("Détection du diabète")
    print(Aaliyah_.goal())
    print(Aaliyah_.train(donnees_sante, categories_sante))
    print(Aaliyah_.answer_to([64, 52, 16]))