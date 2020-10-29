from PIL import Image,ImageDraw,ImageFont

# Laad de achtergrond afeebdling in de variabele: achtergrond
achtergrond = Image.open("meme_background.jpg")

# Afmetingen opslaan in eigen variabelen
breedte = achtergrond.width
hoogte = achtergrond.height

# Laad het Impact lettertype
lettertype = ImageFont.truetype("impact.ttf", 12)

# Vraag aan de ImageDraw module om een tekengebied te maken op de achtergrond afbeelding
tekengebied = ImageDraw.Draw(achtergrond)

# Tekst schrijven
tekst = "When the boys comes together\nAfter Quarantine"

# Zet hier de code met de berekeningen
tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype) 
print("tekstbreedte=" + str(tekst_breedte) + ", tekst_hoogte=" + str(tekst_hoogte))

# Tekst positie berekenen
tekst_x = (breedte - tekst_breedte)/2
tekst_y = (hoogte - tekst_hoogte)/2

tekengebied.multiline_text((tekst_x-2, tekst_y-2), tekst, font=lettertype, fill=(255,255,255))

# Het resultaat tonen
achtergrond.show()

#En opslaan onder een andere naam
achtergrond.save("meme_met_tekst.jpg")



