#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 11:58:09 2020

@author: momcilo
"""
from datetime import date, time
import Pacijenti
import Dijagnoze

#učitavanje iz fajla


def ucitajPreglede():
    with open("pregledi.txt", "r") as f:
        for line in f.readlines():
            if len(line) > 1:
                pregled = strtopre(line)
                pregledi.append(pregled)
            
            
def strtopre(line):
    if line[-1] == '\n':
        line = line[:-1]
        
    pacijent, lekar, datum, termin, dijagnoza = line.split("|")
    dat = date.fromisoformat(datum)
    ter = time.fromisoformat(termin)
    
    pregled = {"pacijent" : pacijent,
               "lekar" : lekar, 
               "datum" : dat,
               "termin" : ter,
               "dijagnoza" : dijagnoza}
    
    return pregled

#proverava da li je lista pregleda prazna


def prazno():
    if pregledi == []:
        return True
    return False


#operacije koje menjaju sadržaj liste pregleda


def azurirajPreglede(**kwargs):
    global pregledi
    if kwargs is not None:
        pregledi = [p for p in pregledi if not selekcija(p, **kwargs)]


def selekcija(pregled, **kwargs):
    t = True
    if kwargs is not None:
        for key,value in kwargs.items():
            if pregled[key] != value:
                t = False
    return t


def zakaziPregled(pregled):
    global pregledi
    pregledi.append(pregled)
   

def otkaziPregled(p):
    global pregledi
    pregledi.remove(p)
    

def ucitajDatum():
    while(True):
        try:
            dan = eval(input("dan: " ))
            mesec = eval(input("mesec: "))
            godina = eval(input("godina: "))
            d = date(godina, mesec, dan)
            return d
        except ValueError:
            print("Brojevi izvan opsega!")
        except NameError:
            print("Unesite brojeve!")
        except SyntaxError:
            print("Neispravan unos!")


def ucitajTermin():
    while (True):
        try:
            h = eval(input("Sati: "))
            t = time(h)
            return t
        except ValueError:
            print("Broj izvan opsega!")
        except NameError:
            print("Unesite broj!")
        except SyntaxError:
            print("Neispravan unos!")


#upisuje listu u fajl


def sacuvajPreglede():
    f = open("pregledi.txt", "w")
    for p in pregledi:
        f.write(pretostr(p))
        f.write("\n")
    f.close()


def pretostr(pregled):
    return "|".join([pregled["pacijent"], 
                     pregled["lekar"], 
                     pregled["datum"].isoformat(),
                     pregled["termin"].isoformat(), 
                     pregled["dijagnoza"]])   


#pronalazi preglede koji odgovaraju selekciji


def nadjiPregled(**kwargs):
    if kwargs is not None:
        lista = [p for p in pregledi if selekcija(p, **kwargs)]
    else:
        lista = pregledi
    return lista


def slobodniTermini(lekar, datum):
    pom = {"lekar" : lekar,
           "datum" : datum}
    
    lista = nadjiPregled(**pom)
    sviTer = sviTermini()
    for l in lista:
        sviTer.remove(l["termin"])
    return sviTer


def sviTermini():
    lista = []
    for h in range(8,14):
        t = time(h)
        lista.append(t)
    return lista


# obavljanje pregleda


def obaviPregled(index):
    global pregledi
    Dijagnoze.ispisiDijagnoze()
    while(True):
        naziv = input("Unesite naziv dijagnoze: ")
        dijagnoza = Dijagnoze.nadjiDijagnozu(naziv)
        if dijagnoza == {} or naziv == "Nema":
            print("Uneli ste neispravnu dijagnozu: ")
        else:
            pregledi[index]["dijagnoza"] = naziv
            break


#ispis pregleda


def zaglavljePregledi():
    return "pacijent      |lekar               |datum     |termin  |dijagnoza           \n" \
           "--------------+--------------------+----------+--------+--------------------"


def formatirajPregled(pregled):
    return "{0:14}|{1:20}|{2:10}|{3:8}|{4:20}".format(pregled["pacijent"], 
                                                      pregled["lekar"],
                                                      pregled["datum"].isoformat(), 
                                                      pregled["termin"].isoformat(),
                                                      pregled["dijagnoza"])


def ispisiPreglede(lista):
    if lista == []:
           print("Nema pregleda!")
           return
      
    print(zaglavljePregledi())
    for l in lista:
        print(formatirajPregled(l))


pregledi = []
ucitajPreglede()