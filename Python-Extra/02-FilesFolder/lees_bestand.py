# Hier importeer io module

import io

# Bestand in read-only (r) mode openen
bestand2 =  open("test.txt","r")

# Alle tekst lezen met read() en opslaan in variabele: inhoud
inhoud = bestand2.read()

# De inhoud op het scherm zetten:
print("De inhoud van het bestand is:")
print(inhoud)
