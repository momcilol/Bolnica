#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 19:24:49 2020

@author: momcilo
"""

def login(username, password):
    for l in lekari:
        if l['username'] == username and l['password'] == password:
            return True
    return False


#############################


def ucitajLekare():
    f = open("lekari.txt", "r")
    lekar = {}
    for line in f.readlines():
        if len(line) > 1:
            lekar = strtolek(line)
            lekari.append(lekar)
    f.close()


def strtolek(line):
    if line[-1] == '\n':
        line = line[:-1]
    lekar = {}
    lekar["ime"], lekar["prezime"], lekar["username"], lekar["password"] = line.split("|")
    return lekar


##############################


def zaglavljeLekar():
    return "Ime       |Prezime        |username            \n" \
           "----------+---------------+--------------------"


def formatirajLekara(lekar):
    return "{0:10}|{1:15}|{2:20}".format(lekar["ime"], lekar["prezime"], lekar["username"])

    
def ispisiLekare():
    print(zaglavljeLekar())
    for l in lekari:
        print(formatirajLekara(l))


lekari = []
ucitajLekare()
