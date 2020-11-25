# Hier importeer je de os module

import os


# De huidige directory opvragen en oplsaan in de variabele: werkmap

werkmap = os.getcwd()



# De letters cwd staan voor: current working directory (dehuidigemap!)


# Op scherm printen
print("De huidige map is:"+werkmap)

os.mkdir("een nieuwe map")

#Gebruiker om de naam van de map vragen

mapnaam = input("Welke naam wil je voor de map?")


# Als lengte van mapnaam > 0 is dan maken we de map
lengte_mapnaam = len(mapnaam)

if lengte_mapnaam > 0:
    os.mkdir(mapnaam)
    print("De map" + mapnaam + "is gemaakt.")
else:
    print("Je hebt geen naam ingevoerd")
