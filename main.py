import random
import os
os.system('color 4F')
os.system('cls')
print("Herzlich Willkommen ")
print("--------------------\n")
points = int()
def banner():
    print("\n")
    print(r" \ \        / /          | |  / ____|")
    print(r"  \ \  /\  / /__  _ __ __| | | |  __ _   _  ___  ___ ___  ___ _ __ "+"    "+"Deine Punkte:")
    print(r"   \ \/  \/ / _ \| '__/ _` | | | |_ | | | |/ _ \/ __/ __|/ _ \ '__|"+"    "+str(points))
    print(r"    \  /\  / (_) | | | (_| | | |__| | |_| |  __/\__ \__ \  __/ |   ")
    print(r"     \/  \/ \___/|_|  \__,_|  \_____|\__,_|\___||___/___/\___|_|   ")
    print("\nErrate das Wort! Jeder Versuch kostet dich 100 Punkte!")
    print("----------------------------------------")


schwierigkeitsgrad = input("Wähle einen Schwierigkeitsgrad: (einfach/mittel/schwer)\n")
while schwierigkeitsgrad not in ("einfach", "mittel", "schwer"):
    os.system('cls')
    schwierigkeitsgrad = input("Ungültige Eingabe! Wähle einen Schwierigkeitsgrad: (einfach/mittel/schwer)\n")

if schwierigkeitsgrad == "einfach":
    points = 2000
elif schwierigkeitsgrad == "mittel":
    points = 500
elif schwierigkeitsgrad == "schwer":
    points = 200
    os.system('cls')
words = ("Abenteuer", "Bibliothek", "Chaos", "Diamant", "Eleganz", "Fantasie", "Gitarre", "Harmonie",
         "Inspiration", "Jazz", "Kreativität", "Leidenschaft", "Melodie", "Natur", "Orchester", "Poesie",
         "Qualität", "Rhythmus", "Symmetrie", "Tanz")

choosen_word = random.choice(words)
def game():
    global points, chosen_word, banner
    banner()
    user_input = input("          ")




    if choosen_word == "Abenteuer":
        hint = "Ein Wort, das die Neugierde weckt und oft mit Reisen und Entdeckungen in Verbindung gebracht wird."
    if choosen_word == "Bibliothek":
        hint = "Ein Ort, an dem Wissen und Geschichten gesammelt sind, aber es geht nicht nur um Bücher."
    if choosen_word == "Chaos":
        hint = "Ein Zustand der Unordnung, in dem Dinge durcheinander sind und schwer zu verstehen."
    if choosen_word == "Diamant":
        hint = "Ein kostbarer Edelstein, der unter Druck entsteht und oft als Symbol für Liebe verwendet wird."
    if choosen_word == "Eleganz":
        hint = "Ein Begriff, der mit Stil, Klasse und raffinierter Schönheit in Verbindung steht."
    if choosen_word == "Fantasie":
        hint = "Die Fähigkeit, sich Dinge vorzustellen, die nicht real sind, aber dennoch inspirierend wirken."
    if choosen_word == "Gitarre":
        hint = "Ein Musikinstrument mit Saiten, das oft von Künstlern gespielt wird."
    if choosen_word == "Harmonie":
        hint = "Ein Zustand, in dem verschiedene Elemente friedlich zusammenwirken."
    if choosen_word == "Inspiration":
        hint = "Etwas, das Ideen und Kreativität anregt, aber nicht immer offensichtlich ist."
    if choosen_word == "Jazz":
        hint = "Eine Musikrichtung, die Improvisation und Leidenschaft vereint."
    if choosen_word == "Kreativität":
        hint = "Die Fähigkeit, etwas Einzigartiges zu schaffen, das aus dem Herzen kommt."
    if choosen_word == "Leidenschaft":
        hint = "Ein intensives Gefühl oder eine Hingabe zu etwas, das das Herz schneller schlagen lässt."
    if choosen_word == "Melodie":
        hint = "Eine Abfolge von Tönen, die eine musikalische Geschichte erzählt."
    if choosen_word == "Natur":
        hint = "Die Welt um uns herum, einschließlich Pflanzen, Tiere und Landschaften."
    if choosen_word == "Orchester":
        hint = "Eine Gruppe von Musikern, die zusammen spielen und eine beeindruckende Klangvielfalt erzeugen."
    if choosen_word == "Poesie":
        hint = "Eine künstlerische Form der Sprache, die oft metaphorisch und tiefgründig ist."
    if choosen_word == "Qualität":
        hint = "Ein Maßstab für Exzellenz und Wert."
    if choosen_word == "Rhythmus":
        hint = "Die pulsierende Kraft, die Musik und Bewegung antreibt."
    if choosen_word == "Symmetrie":
        hint = "Eine ausgewogene Anordnung von Teilen, die oft als ästhetisch empfunden wird."
    if choosen_word == "Tanz":
        hint = "Eine körperliche Ausdrucksform, die Freude, Leidenschaft und Bewegung vereint."
    if points <= 100:
        print("Schade, du hast verloren. Das gesuchte Wort war: "+choosen_word)
        exit()


    if user_input == choosen_word:
        os.system('cls')
        banner()
        print("\nDU HAST GEWONNEN!!!")
    elif user_input != choosen_word:
        os.system('cls')
        points = points - 100
        print("Falsches Wort. Versuche es nochmal\n")
        if points == 1900 or points == 400 or points == 300:
            print("Tipp: "+hint+"\n")
        game()


game()
