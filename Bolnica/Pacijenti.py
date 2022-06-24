#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 13:12:03 2020

@author: momcilo
"""

#učitavanje iz fajla


def ucitajPacijente():
    f = open("pacijenti.txt", "r")
    for line in f.readlines():
        if len(line) > 1:
            pacijenti.append(strtopac(line))
    f.close()


def strtopac(line):
    if line[-1] == '\n':
        line = line[:-1]
    pacijent = {}
    pacijent["ime"], pacijent["prezime"], pacijent["JMBG"] = line.split("|")
    return pacijent

######################


def prazno():
    if pacijenti == []:
        return True
    return False


#izmena sadržaja liste "pacijenti"


def dodajPacijenta(pacijent):
    pacijenti.append(pacijent)


def izbrisiPacijenta(pacijent):
    pacijenti.remove(pacijent)


def imaJMBG(JMBG, lista):
    if "JMBG" in lista[0]:
        key = "JMBG"
    else:
        key = "pacijent"
    for pom in lista:
        if JMBG == pom[key]:
            return True
    return False


def ispravanJMBG(JMBG):
    if not(len(JMBG) == 13) or not(JMBG.isdigit()):
        print("JMBG je broj od 13 cifara")
        return False
    return True


#upisuje sadržaj liste nazad fajl


def sacuvajPacijente():
    f = open("pacijenti.txt", "w")
    for p in pacijenti:
        f.write(pactostr(p))
        f.write("\n")
    f.close()


def pactostr(pacijent):
    return "|".join([pacijent["ime"], pacijent["prezime"], pacijent["JMBG"]])    
  

#vraca listu pacijenata koja odgovara selekciji


def nadjiPacijenta(**kwargs):
    lista = [l for l in pacijenti if selekcija(l, **kwargs)]
    return lista


def selekcija(pacijent, **kwargs):
    if kwargs is not None:
        for key,value in kwargs.items():
            if pacijent[key] != kwargs[key]:
                return False
    return True


#ispis liste pacijenata


def zaglavljePacijenti():
    return "Ime       |Prezime     |JMBG         \n" \
           "----------+------------+-------------"

        
def formatirajPacijent(pacijent):
    return "{0:10}|{1:12}|{2:13}".format(pacijent["ime"], pacijent["prezime"], pacijent["JMBG"])

    
def ispisiPacijente(lista):
    print(zaglavljePacijenti())
    for p in lista:
        print(formatirajPacijent(p))

    
pacijenti = [] 
ucitajPacijente()