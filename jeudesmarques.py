import colorama
from termcolor import colored

from PyInquirer import prompt

colorama.init()

is_running = True

colorama.init()
while is_running:

    print(colored("Bienvenue sur le jeu des marques de cartes meres et pc potables ou fixes oem v1.1","red"))

    print(colored("Si ta carte mere pue ben tu le verra,''tu peux mettre une marque de pc'' ","blue"))

    QUESTION = {
        "type": "list",  # Ne pas retirer
        "name": "command",  # Ne pas retirer
        "message": "Choisissez un type de pc",  # Question

        # Choix
        "choices": [
            "Carte Mere",
            "Pc Fixe",
            "Pc Portable"
        ]
    }

    reponse = prompt(QUESTION).get('command')
    print(reponse)

    if reponse == "Carte Mere":

        carte_mere = input("Met ta marque de carte mere: ").lower()

        print(carte_mere)

        if carte_mere == "asrock":
            print(colored("Ca va en vrai","blue"))

        elif carte_mere == "asus":
            print(colored("Gangifié","red"))

        elif carte_mere == "biostar":
            print(colored("Chintokifié","green"))

        elif carte_mere == "gigabyte":
            print(colored("élite et respect","magenta"))

        elif carte_mere == "intel desktop board":
            print(colored("haha élite ta le son intel de demarrage","cyan"))

        elif carte_mere == "msi":
            print(colored("duuuuuuu gange sur les mises a jour du bios sinon ca va","red"))

        elif carte_mere == "nzxt":
            print(colored("Woaw ta des thunes ptn élite !","yellow"))

        elif carte_mere == "evga":
            print(colored("correct !","white"))

        elif carte_mere == "foxconn":
            print(colored("ta un pc prémonté de l'epoque ? ouch courrage","yellow"))

        elif carte_mere == "ecs":
            print(colored("C'est quoi ce truc ?","red"))

        elif carte_mere == "colorful":
            print(colored("LA COULLLEUUURRRRR","blue"))

        elif carte_mere == "sapphire":
            print(colored("élite", "white"))

        elif carte_mere == "pc":
            print(colored("alors mec met une marque pas pc xD","red"))

    elif reponse == "Pc Fixe":
        pc_fixe = input("Met ta marque de ton pc fixe: ").lower()

        print(pc_fixe)

        if pc_fixe == "megaport":
            print(colored("DU GAAAAANNNNNNGGGGGEEEEE","red"))

        elif pc_fixe == "hp":
            print(colored("duuuuuuu gange sur les pavillons bas de gamme sinon correct","red"))

        elif pc_fixe == "dell":
            print(colored("élite sur les pc pros mais pc gamer c'est de la merde","blue"))

        elif pc_fixe in ["apple", "mac", "imac"]:
            print(colored("Sale riche !!!! xD","yellow"))

        elif pc_fixe == "lenovo":
            print(colored("Gangifié sur certains models hein thinkpad ;) mais sinon ca va ","red"))

        elif pc_fixe == "packard bell":
            print(colored("PACKARD POUBELLE !!!!!!!!!!","red"))

        elif pc_fixe == "compaq":
            print(colored("Je sais pas ...","yellow"))

        elif pc_fixe == "ibm":
            print(colored("Ton pc a 250 ans ou quoi ?","green"))

        elif pc_fixe in ["powerbook", "powermac", "powerpc", "g4"]:
            print(colored("Tu arrive a lancer mon jeu sur ton pc ? et ben bravo !!! ","white"))

        elif pc_fixe == "medion":
            print(colored("Ton pc a 400ans ? et ben !","yellow"))

        elif pc_fixe == "fujitsu":
            print(colored("pc du bahut xD","white"))

        elif pc_fixe == "pc":
            print(colored("alors mec met une marque pas pc xD","red"))

        elif pc_fixe == "acer":
            print(colored("élite sinon tu est liptonaceriste ? ","white"))

    elif reponse == "Pc Portable":

        pc_portable = input("Met ta marque de ton pc portable: ").lower()

        print(pc_portable)

        if pc_portable == "acer":
            print(colored("élite sinon tu est liptonaceriste ? ","white"))

        elif pc_portable == "hp":
            print(colored("duuuuuuu gange","red"))

        elif pc_portable == "lenovo":
            print(colored("THINKPAD C'EST DE LA DAUBE !!!","red"))

        elif pc_portable in ["apple", "mac", "macbook"]:
            print(colored("Sale riche !!!! xD","yellow"))

    action = input("Appuie sur ''r'' pour recommencer où ''q'' pour quitter")

    if action == 'q':
        is_running = False

    elif action != 'r':
        print("action invalide")
