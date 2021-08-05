import colorama
from termcolor import colored

colorama.init()

is_running = True

colorama.init()
while is_running:

    print("Si ta carte mere pue ben tu le verra ''tu peux mettre une marque de pc'' ")

    marque = input("Met ta marque de carte mere ou de ton pc : ").lower()

    print(marque)

    if marque == "megaport":
        print(colored("DU GAAAAANNNNNNGGGGGEEEEE","red"))

    elif marque == "asrock":
        print(colored("Ca va en vrai","blue"))

    elif marque == "asus":
        print(colored("Gangifié","red"))

    elif marque == "biostar":
        print(colored("Chintokifié","green"))

    elif marque == "gigabyte":
        print(colored("élite et respect","magenta"))

    elif marque == "intel desktop board":
        print(colored("haha élite ta le son intel de demarrage","cyan"))

    elif marque == "msi":
        print(colored("duuuuuuu gange sur les mises a jour du bios sinon ca va","red"))

    elif marque == "hp":
        print(colored("duuuuuuu gange sur les pavillons bas de gamme sinon correct","red"))

    elif marque == "dell":
        print(colored("élite sur les pc pros mais pc gamer c'est de la merde","blue"))

    elif marque in ["apple", "mac", "macbook", "imac"]:
        print(colored("Sale riche !!!! xD","yellow"))

    elif marque == "lenovo":
        print(colored("Gangifié sur certains models hein thinkpad ;) mais sinon ca va ","red"))

    elif marque == "packard bell":
        print(colored("PACKARD POUBELLE !!!!!!!!!!","red"))

    elif marque == "compaq":
        print(colored("Je sais pas ...","yellow"))

    elif marque == "ibm":
        print(colored("Ton pc a 250 ans ou quoi ?","green"))

    elif marque in ["powerbook","powermac","powerpc","g4"]:
        print(colored("Tu arrive a lancer mon jeu sur ton pc ? et ben bravo !!! ","white"))

    elif marque == "medion":
        print(colored("Ton pc a 400ans ? et ben !","yellow"))

    elif marque == "nzxt":
        print(colored("Woaw ta des thunes ptn élite !","yellow"))

    elif marque == "evga":
        print(colored("correct !","white"))

    elif marque == "foxconn":
        print(colored("ta un pc prémonté de l'epoque ? ouch courrage","yellow"))

    elif marque == "ecs":
        print(colored("C'est quoi ce truc ?","red"))

    elif marque == "colorful":
        print(colored("LA COULLLEUUURRRRR","blue"))

    elif marque == "fujitsu":
        print(colored("pc du bahut xD","white"))

    elif marque == "pc":
        print(colored("alors mec met une marque pas pc xD","red"))

    elif marque == "sapphire":
        print(colored("élite","white"))

    elif marque == "acer":
        print(colored("élite sinon tu est liptonaceriste ? ","white"))

    action = input("Appuie sur ''r'' pour recommencer où ''q'' pour quitter")

    if action == 'q':
        is_running = False

    elif action != 'r':
        print("action invalide")
