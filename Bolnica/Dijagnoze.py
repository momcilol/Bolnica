#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:33:58 2020

@author: momcilo

"""

#učitavanje iz fajla


def ucitajDijagnoze():
    with open("dijagnoze.txt", "r") as f:
        for line in f.readlines():
            dijagnoze.append(strtodij(line))
        

def strtodij(line):
    if line[-1] == '\n':
        line = line[:-1]
    dijagnoza = {}
    dijagnoza["naziv"], dijagnoza["opis"] = line.split("|")
    return dijagnoza


#provera da li je lista dijagnoza prazna


def prazno():
    if dijagnoze == []:
        return True
    return False


#izmena sadržaja liste "dijagnoze"


def dodajDijagnozu(dijagnoza):
    dijagnoze.append(dijagnoza)


def imaDijagnoza(naziv):
    for d in dijagnoze:
        if d["naziv"].lower() == naziv.lower():
            return True
    return False


def nadjiDijagnozu(naziv):
    for d in dijagnoze:
        if d["naziv"].lower() == naziv.lower():
            return d
    return {}


def ukloniDijagnozu(dijagnoza):
    dijagnoze.remove(dijagnoza)


#upisuje sadržaj liste nazad u fajl


def sacuvajDijagnoze():
    f = open("dijagnoze.txt", "w")
    for d in dijagnoze:
        f.write(dijtostr(d))
        f.write("\n")
    f.close()


def dijtostr(dijagnoza):
    return "|".join([dijagnoza["naziv"], dijagnoza["opis"]])


#ispis dijagnoze


def formatirajDijagnozu(dijagnoza):
    return "naziv: {0}\nopis: {1}\n".format(dijagnoza["naziv"], dijagnoza["opis"])


def ispisiDijagnoze():
    for d in dijagnoze:
        print(formatirajDijagnozu(d))


dijagnoze = []
ucitajDijagnoze()