#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 12:32:16 2020

@author: momcilo
"""

from datetime import date, datetime, time
import Lekari
import Pacijenti
import Pregledi
import Dijagnoze
import matplotlib.pyplot as plt


def main():
    for i in range(1, 6):
        if i == 5 and not(login()):
            print("Iskoristili ste sve pokušaje. Doviđenja!")
            return
        if(not(login())):
            print("Pogrešan unos, ostalo vam je {0} pokušaja!".format(5-i))
        else:
            break
    komanda = ""
    while komanda != 'X':
        komanda = menu()
        ####################
        if komanda == '1':
            nadjiPacijenta()
        elif komanda == '2':
            ispisiPacijente()
        elif komanda == '3':
            dodajPacijenta()
        elif komanda == '4':
            ukloniPacijenta()
        ####################
        elif komanda == '5':
            nadjiPregled()
        elif komanda == '6':
            ispisiPreglede()
        elif komanda == '7':
            zakaziPregled(username)
        elif komanda == '8':
            obaviPregled(username)
        elif komanda == '9':
            otkaziPregled(username)
        ####################
        elif komanda == '10':
            ispisiLekare()
        ####################
        elif komanda == '11':
            ispisiDijagnoze()
        elif komanda == '12':
            dodajDijagnozu()
        elif komanda == '13':
            ukloniDijagnozu()
        elif komanda == '14':
            nadjiDijagnozu()
        ####################
        elif komanda == '15':
            brPregledaPoLek()
        elif komanda == '16':
            brPregledaPoPac()
        elif komanda == '17':
            brPregledaPoDij()
    Dijagnoze.sacuvajDijagnoze()
    Pacijenti.sacuvajPacijente()
    Pregledi.sacuvajPreglede()
    print("Doviđenja.")


def login():
    global username
    username = input("Unesite vas username: ")
    password = input("Unesite vas password: ")
    return Lekari.login(username, password)


def menu():
    printMenu()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4', '5', '6', '7',
                                  '8', '9', '10', '11', '12', '13',
                                  '14', '15', '16', '17', 'X'):
        print( "Uneli ste pogresnu komandu, pokusajte ponovo: ")
        printMenu()
        command = input(">> ")
    return command.upper()


def printMenu():
    print( "\nIzaberite opciju:")
    print( "  Operacije vezane za pacijenta: ")
    print( "  1 - pronađite pacijenta")
    print( "  2 - ispišite listu svih pacijenata")
    print( "  3 - dodajte novog pacijenta")
    print( "  4 - uklonite pacijenta")
    print( "  Operacije vezane za preglede: ")
    print( "  5 - pronađite pregled")
    print( "  6 - ispišite listu pregleda")
    print( "  7 - zakazite pregled pacijentu")
    print( "  8 - obavite pregled")
    print( "  9 - otkažite pregled")
    print( "  Operacije vezane za lekare: ")
    print( " 10 - ispišite listu svih lekara")
    print( "  Operacije vezane za dijagnoze: ")
    print( " 11 - ispišite listu svih dijagnoza")
    print( " 12 - dodajte dijagnozu")
    print( " 13 - uklonite dijagnozu")
    print( " 14 - nađi dijagnozu")
    print( "  Operacije vezane za statistiku: ")
    print( " 15 - prikaz broja pregleda po lekaru")
    print( " 16 - prikaz broja pregleda po pacijentu")
    print( " 17 - prikaz broja pregleda po dijagnozi")
    print( "  x - izlaz iz programa")


#operacije vezane za pacijenta


def nadjiPacijenta():
    if Pacijenti.prazno():
        print("Trenutno ne postoji nijedan sačuvan pacijent!")
        return

    pacijent = {}

    t = input("Znate li pacijentvo ime? [da - ukoliko znate]: ")
    if t.lower() == 'da':
        pacijent["ime"] = input("Unesite ime pacijenta: ")

    t = input("Znate li pacijentvo prezime? [da - ukoliko znate]: ")
    if t.lower() == 'da': 
        pacijent["prezime"] = input("Unesite prezime pacijenta: ")
    
    
    t = input("Znate li pacijentov JMBG? [da - ukoliko znate]: ")
    if t.lower() == 'da':
        pacijent["JMBG"] = input("Unesite JMBG pacijenta: ")
    
    lista = Pacijenti.nadjiPacijenta(**pacijent)
    if lista == []:
        print("Nema pacijenata koji odgovaraju vasoj pretrazi.")
    else:
        Pacijenti.ispisiPacijente(lista)


def ispisiPacijente():
    if Pacijenti.prazno():
        print("Trenutno ne postoji nijedan sačuvan pacijent!")
        return
    Pacijenti.ispisiPacijente(Pacijenti.pacijenti)


def dodajPacijenta():
    pacijent = {}
    
    JMBG = input("Unesite JMBG: ")
    while(not(Pacijenti.ispravanJMBG(JMBG)) or \
          Pacijenti.imaJMBG(JMBG,Pacijenti.pacijenti)):
        JMBG = input("Unesite JMBG: ")
    
    pacijent["JMBG"] = JMBG
    pacijent["ime"] = input("Unesite ime pacijenta: ")
    pacijent["prezime"] = input("Unesite prezime pacijenta: ")
    Pacijenti.dodajPacijenta(pacijent)


def ukloniPacijenta():
    if Pacijenti.prazno():
        print("Nema nijednog pacijenta.")
    else:
        JMBG = ""
        Pacijenti.ispisiPacijente(Pacijenti.pacijenti)
        
        
        while(True):
            JMBG = input("Unesite JMBG pacijenta kojeg zelite da uklonite: ")
            pacijent = {"JMBG" : JMBG}
            pac = Pacijenti.nadjiPacijenta(**pacijent)
            if pac == []:
                print("Nema pacijenta s tim JMBG-om!")
            else:
                Pacijenti.izbrisiPacijenta(pac[0])
                pacijent = { "pacijent" : JMBG }
                Pregledi.azurirajPreglede(**pacijent)
                return


#operacije vezane za preglede


def nadjiPregled():
    if Pregledi.prazno():
        print("Trenutno ne postoji nijedan zakazan pregled!")
        return
    
    pregled = {}
    
    t = input("Znate li pacijentov JMBG? [da - ukoliko znate]: ")
    if t.lower() == 'da':
        pregled["pacijent"] = input("Unesite JMBG pacijenta: ")
    
    t = input("Znate li username lekara? [da - ukoliko znate]: ")
    if t.lower() == 'da': 
        pregled["lekar"] = input("Unesite ime pacijenta: ")
    
    t = input("Znate li datum pregleda? [da - ukoliko znate]: ")
    if t.lower() == 'da': 
        pregled["datum"] = Pregledi.ucitajDatum()
    
    t = input("Znate li termin pregleda? [da - ukoliko znate]: ")
    if t.lower() == 'da':
        pregled["termin"] = Pregledi.ucitajTermin()
    
    t = input("Znate li dijagnozu pregleda? [da - ukoliko znate]: ")
    if t.lower() == 'da':
        pregled["dijagnoza"] = input("Unesite naziv dijagnoze: ")
    
    lista = Pregledi.nadjiPregled(**pregled)
    if lista == []:
        print("Nema pregleda koji odgovaraju vasoj pretrazi.")
    else:
        Pregledi.ispisiPreglede(lista)


def ispisiPreglede():
    if Pregledi.prazno():
        print("Trenutno ne postoji nijedan zakazan pregled!")
        return
    
    Pregledi.ispisiPreglede(Pregledi.pregledi)


def obaviPregled(username):
    if Pregledi.prazno():
        print("Trenutno ne postoji nijedan zakazan pregled!")
        return
    
    pregled = {"lekar" : username,
               "datum" : date.today(),
               "termin" : time(datetime.now().time().hour, 0, 0)}
    
    lista = Pregledi.nadjiPregled(**pregled)
    if lista == []:
        print("Trenutno nemate zakazan nijedan pregled za ovo vreme.")
    else:
        i = Pregledi.pregledi.index(lista[0])
        Pregledi.obaviPregled(i)


def zakaziPregled(username):
    Pacijenti.ispisiPacijente(Pacijenti.pacijenti)
    JMBG = input("Unesite JMBG pacijenta: ")
    
    while(not(Pacijenti.imaJMBG(JMBG, Pacijenti.pacijenti))):
        JMBG = input("Nema takvog pacijeta, unesite novi JMBG: ")
    
    while(True): 
        print("Danas je: {0}\nUnesite za kada zelite da " \
                  "zakazete pregled: ".format(date.today()))
        datum = Pregledi.ucitajDatum()
        if datum <= date.today(): 
            print("Mozete da zakazujete samo za naredne dane!")
        elif datum.weekday() == 5 or datum.weekday() == 6:
            print("Nema pregleda vikendom!")
        elif Pregledi.slobodniTermini(username, datum) == []:
            print("svi termini za taj dan su zauzeti: ")
        else:
            break
    
    termini = []
    termini = Pregledi.slobodniTermini(username,datum)
        
    while(True):
        print("Izaberite neke od slobodnih termina")
        
        for t in termini:
            print(t.isoformat(timespec = "minutes"))
        print("U koliko sati zelite pregled?")
        ter = Pregledi.ucitajTermin()
        if ter not in termini:
            print("Izabrali ste pogresan termin")
        else:
            break
        
        
    pregled = {"pacijent" : JMBG,
               "lekar" : username, 
               "datum" : datum,
               "termin" : ter, 
               "dijagnoza" : "Nema"}
    
    Pregledi.zakaziPregled(pregled)


def otkaziPregled(username):
    if Pregledi.prazno():
        print("Trenutno ne postoji nijedan zakazan pregled!")
        return
    
    pregled = {"lekar" : username,
               "dijagnoza" : "Nema"}
    
    lista = Pregledi.nadjiPregled(**pregled)
    Pregledi.ispisiPreglede(lista)  
    
    if lista == {}:
        print("Trenutno nemate nijedan zakazan pregled!")
        return
    
    JMBG = input("Unesite JMBG pacijenta: ")
    while(not(Pacijenti.imaJMBG(JMBG, lista))):
        JMBG = input("Nema takvog pacijeta, unesite JMBG: ")
        
    pregled["pacijent"] = JMBG
    
    while(True): 
        print("Danas je: {0}\nUnesite datum pregleda koji " \
              "zelite da otkazete: ".format(date.today()))
        datum = Pregledi.ucitajDatum()
        print("Unesite u koliko sati je pregled.")
        termin = Pregledi.ucitajTermin()
        
        if datum < date.today() or \
        (datum == date.today() and termin <= datetime.now().time()): 
            print("Mozete da otkazujete preglede koji tek treba da se obave!")
        elif datum.weekday() == 5 or datum.weekday() == 6:
            print("Nema pregleda vikendom!")
        else:
            pregled["datum"] = datum
            pregled["termin"] = termin
            pom = Pregledi.nadjiPregled(**pregled)
            if pom != []:
                break
    
    Pregledi.otkaziPregled(pom[0])


#operacije vezane za lekare


def ispisiLekare():
    Lekari.ispisiLekare()
    
    
#operacije vezane za dijagnoze


def ispisiDijagnoze():
    if Dijagnoze.prazno():
        print("Trenutno ne postoji nijedna sačuvana dijagnoza!")
        return
    
    Dijagnoze.ispisiDijagnoze()
    
    
def dodajDijagnozu():
   dijagnoza = {}
   while True:
       dijagnoza["naziv"] = input("Unesite naziv dijagnoze: ")
       if not(Dijagnoze.imaDijagnoza(dijagnoza["naziv"])):
           break
       else:
           print("Uneli ste postojecu dijagnozu")
           
   dijagnoza["opis"] = input("Opišite dijagnozu: ")
   Dijagnoze.dodajDijagnozu(dijagnoza)
   
 
def ukloniDijagnozu():
    if Dijagnoze.prazno():
        print("Trenutno ne postoji nijedna sačuvana dijagnoza!")
        return
    
    while True:
        naziv = input("Unesite naziv dijagnoze: ")
        dijagnoza = Dijagnoze.nadjiDijagnozu(naziv)
        if dijagnoza == {}:
            print("Uneli ste nepostojecu dijagnozu")
        elif naziv == "Nema" or naziv == "Zdrav":
            print("Ne možete obrisati dijagnoze \"Zdrav\" i \"Nema\"")            
        else:
            Dijagnoze.ukloniDijagnozu(dijagnoza)
            d = {"dijagnoza" : naziv}
            Pregledi.azurirajPreglede(**d)
            return


def nadjiDijagnozu():
    if Dijagnoze.prazno():
        print("Trenutno ne postoji nijedna sačuvana dijagnoza!")
        return
    
    naziv = input("Unesite naziv dijagnoze: ")
    dijagnoza = Dijagnoze.nadjiDijagnozu(naziv)
    if dijagnoza == {}:
        print("Nema dijagnoze sa tim nazivom: ")
    else:
        print(Dijagnoze.formatirajDijagnozu(dijagnoza))


#operacije vezane za statistiku


def brPregledaPoLek():
    lista = []
    
    for l in Lekari.lekari:
        pom = {"lekar" : l["username"]}
        v = len(Pregledi.nadjiPregled(**pom))
        s = " ".join([l["ime"], l["prezime"]])
        lista.append({"ime" : s, "broj pregleda" : v})
    
    lista.sort(key = lambda x: x["broj pregleda"])
    x_osa = []
    y_osa = []
    for l in lista:
        x_osa.append(l["ime"])
        y_osa.append(l["broj pregleda"])
    plt.bar(x_osa, y_osa)
    plt.xlabel("lekari")
    plt.xticks(rotation=90)
    plt.ylabel("broj pregleda")
    plt.ylim(ymin = 0, ymax=10)
    plt.show()
    

def brPregledaPoPac():
    lista = []
    
    for p in Pacijenti.pacijenti:
        pom = {"pacijent" : p["JMBG"]}
        v = len(Pregledi.nadjiPregled(**pom))
        s = " ".join([p["ime"], p["prezime"]])
        lista.append({"ime" : s, "broj pregleda" : v})
    
    lista.sort(key = lambda x: x["broj pregleda"])
    x_osa = []
    y_osa = []
    for l in lista:
        x_osa.append(l["ime"])
        y_osa.append(l["broj pregleda"])
    plt.bar(x_osa, y_osa)
    plt.xlabel("pacijenti")
    plt.xticks(rotation=90)
    plt.ylabel("broj pregleda")
    plt.ylim(ymin = 0, ymax=10)
    plt.show()



def brPregledaPoDij():
    lista = []
    
    for d in Dijagnoze.dijagnoze:
        pom = {"dijagnoza" : d["naziv"]}
        v = len(Pregledi.nadjiPregled(**pom))
        lista.append({"naziv" : d["naziv"], "broj pregleda" : v})
    
    lista.sort(key = lambda x: x["broj pregleda"])
    x_osa = []
    y_osa = []
    for l in lista:
        x_osa.append(l["naziv"])
        y_osa.append(l["broj pregleda"])
    plt.bar(x_osa, y_osa)
    plt.xlabel("dijagnoze")
    plt.xticks(rotation=90)
    plt.ylabel("broj pregleda")
    plt.ylim(ymin = 0, ymax=10)
    plt.show()


username = ""
print(__name__)
if __name__ == "__main__": 
    main()
