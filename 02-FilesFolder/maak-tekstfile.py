# Hier importeer je de io module

import io

# Zo open je een bestand om naar te schrijven

bestand = open("test.txt", "W")


# Een tekst naar het bestand schrijven
bestand.write("Test 123!");


# Vergeet bestand niet te sluiten!
bestand.close()


# Bestand in read-only (r) mode openen
bestand2 = open("test.txt", "r")


# Een tekst naar het bestand schrijven
bestand2.write("Lekker alles overschrijven")

