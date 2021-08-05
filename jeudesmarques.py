import colorama
from termcolor import colored

colorama.init()

is_running = True

colorama.init()
while is_running:

    print("Si ta carte mere pue ben tu le verra")

    marque = input("Met ta marque de carte mere : ")

    print(marque)

    if marque == "Megaport":
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

    action = input("Appuie sur ''r'' pour recommencer où ''q'' pour quitter")

    if action == 'q':
        is_running = False

    elif action != 'r':
        print("action invalide")
