prijzen = {"aardbei":3,"vanille":3,"chocolade":5}
aanbieding = prijzen["vanille"] * 0.8
reclame_tekst = "Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € " + str(aanbieding)
reclame_tekst2 = reclame_tekst[:63]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split(" ")
for el in reclame_tekst4:
    if len(el)>=5:
        el = el.upper()
    else:
        el = el.lower()
    print (el)
