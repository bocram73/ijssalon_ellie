from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs * (1-korting)} euro."
    return uitvoer
print (aanbieding_1("aardbeid", 4, 0.1))

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for bedrag in inkomsten:
        totaal += bedrag
        btw_bedrag = totaal * btw
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
    return uitvoer

inkomsten =[220,430,125,160,205,90,345]
btw = 0.09

print (inkomsten_totaal(inkomsten,btw))

def laag_en_hoog(mijn_lijst):
    hoog = max(mijn_lijst)
    laag = min(mijn_lijst)
    max_min = [hoog, laag]
    return max_min

mijn_lijst = [220,430,125,160,205,90,345]

print (laag_en_hoog(mijn_lijst))

def gemiddelde(mijn_lijst):
    totaal_lijst = 0
    for telling in mijn_lijst:
        totaal_lijst += telling
        gemiddelde = totaal_lijst / len(mijn_lijst)
    uitvoer = f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."
    return uitvoer

print (gemiddelde(mijn_lijst))

def meervoudig(invoer_lijst):
    uitvoer = laag_en_hoog(invoer_lijst)
    return uitvoer

invoer_lijst = [10,5,3,2,1,2,9]

print (meervoudig(invoer_lijst))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
