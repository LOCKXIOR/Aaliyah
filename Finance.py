from Aaliyah import Aaliyah

# Données : [Revenu annuel (k€), Score de crédit (300-850), Dettes (k€)]

donnees_finance = [
    [65, 750, 10], [25, 520, 35], [80, 800, 5], [30, 580, 20], [95, 710, 15],
    [18, 490, 40], [55, 690, 8], [40, 600, 25], [110, 820, 0], [28, 550, 18],
    [72, 730, 12], [22, 510, 30], [88, 790, 6], [35, 590, 22], [100, 720, 10],
    [20, 480, 38], [58, 680, 9], [42, 610, 23], [120, 840, 2], [26, 540, 19],
    [68, 740, 11], [24, 530, 33], [82, 780, 7], [32, 570, 21], [90, 700, 14],
    [19, 500, 36], [60, 670, 10], [38, 620, 24], [105, 810, 4], [29, 560, 17],
    [75, 760, 8], [23, 515, 32], [85, 795, 5], [34, 585, 20], [98, 725, 12],
    [21, 495, 37], [62, 685, 9], [44, 605, 22], [115, 830, 1], [27, 545, 18]
]

categories_finance = [
    "Accordé", "Refusé", "Accordé", "Refusé", "Accordé",
    "Refusé", "Accordé", "Refusé", "Accordé", "Refusé",
    "Accordé", "Refusé", "Accordé", "Refusé", "Accordé",
    "Refusé", "Accordé", "Refusé", "Accordé", "Refusé",
    "Accordé", "Refusé", "Accordé", "Refusé", "Accordé",
    "Refusé", "Accordé", "Refusé", "Accordé", "Refusé",
    "Accordé", "Refusé", "Accordé", "Refusé", "Accordé",
    "Refusé", "Accordé", "Refusé", "Accordé", "Refusé"
]

if __name__=="__main__":
    Aaliyah_=Aaliyah("Estimer la probabilitée d'accord de crédits bancaires")
    print(Aaliyah_.goal())
    print(Aaliyah_.train(donnees_finance,categories_finance))
    print(Aaliyah_.answer_to([120, 850, 10]))
