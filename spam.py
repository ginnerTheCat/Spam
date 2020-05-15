import random

anzahl = input("Gebe ,bitte, die anzahl an! ")
if anzahl == "clear":
    speicher = open("Spam.txt", "w")
    speicher.write("")
    speicher.close()
else:
    anzahl = int(anzahl)
    counter = 1
    while anzahl >= counter:
        try:
            counter += 1
            randomzahl = random.randint(0, 9)
            print(randomzahl)
            speicher = open("Spam.txt", "a")
            speicher.write(str(randomzahl))
            speicher.close()
        except KeyboardInterrupt:
            break
