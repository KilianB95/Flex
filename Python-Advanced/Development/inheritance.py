class Character :

    speed = 10
    points = 0
    sprite = None

    def __init__(self) :
        print("De constructor van Character")

    def walk(self) :
        print("Character loopt met snelheid", self.speed)


class Mario (Character) :

    lives = 3
    item = None

    def __init__(self) :
        # We vullen aan op de onstructoe van de Character:
        super().__init__()
        
        # De snelheid van Mario is standaard hoger:
        self.speed = 30


        # De "walk" fucntionaliteit van Character ga ik OVERSCHRIJVEN
        def walk(self) :
            print("Mario loopt heel anders! Maar wel met de snelheid", self.speed)

    def jump(self) :
        print("Mario springt!!")


# Instanties maken:
characterA = Character()
marioX = Mario()

characterA.walk()
marioX.walk()
marioX.jump()

print(characterA.speed)
print(marioX.speed)
print(marioX.lives)

# Het resultaat verwijst naar de locatie van het volledige object:
print(marioX)