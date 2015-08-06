#####################
#
#	Methodensammlung für Kurs 5.1 Roßleben 2015
#
#	cge 2015_07_21  (1) get_text():             Einlesen einer Texteingabe in einen String
#                                               Input:  - 
#                                               Output: String
#                   (2) get_textfile(str):      Einlesen einer Textdatei in einen String
#                                               Input:  String = Name der Textdatei gespeichert im Ordner "Texte" 
#                                               Output: String
#                   (3) get_key():              Wahl des Schlüssels - Caesar
#                                               Input: -
#                                               Output: Int
#                   (4) transform_text_to_num(str):    Umwandlung eines String in ein Zahlenliste gemäß 26-stelligem Alphabet
#                                               Input: String
#                                               Output: [Int]
#                   (6) transform_num_to_text([int]):  Umwandlung einer Zahlenliste in String gemäß 26-stelligem Alphabet
#                                               Input: [int]
#                                               Output: String
#                   (7) save_textfile(str):     Speichern eines Strings in einer Textdatei
#                                               Input: String
#                                               Name der Textdatei wird nach Aufruf der Funktion gewählt und im Ordner "Texte" gespeichert.

	
import string
import os
import math

ALPHABET_SIZE = 26
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

#Methoden
#1: Texteingabe wird in string gespeichert.
def get_text(): 
    print("Bitte zu verschluesselnden Klartext eingeben:")
    text = input()
    return text
#2: Textdatei wird in string eingelesen.
def get_textfile(name):
    text =""
    try:
        fobj= open("Texte/"+name + ".txt")
        for line in fobj:
            text += line.rstrip()
        fobj.close()
        return text
    except IOError:
        print("Diese Textdatei existiert nicht.")
        os._exit(1)
#3: Einlesen des Schluessels
def get_key():
    print("Schluessel(Zahl)?")
    try:
        schluessel = int(input())
        return schluessel
    except ValueError:
         print("hoppala, das war keine ganze Zahl")
         os._exit(1)
#4: Umwandeln eines Strings in eine Liste von Zahlen
def transform_text_to_num(text):
    zahlenliste = []
    text = text.lower()
    for buchstabe in text:
        if buchstabe in ALPHABET: 
            zahl = (int(ALPHABET.index(buchstabe)))%ALPHABET_SIZE
            zahlenliste.append(zahl)
    return zahlenliste
#6: Umwandeln von Zahlenliste in String
def transform_num_to_text(zahlenliste):
    text = ""
    for i in range(len(zahlenliste)):
        zahl = (zahlenliste[i])%ALPHABET_SIZE
        text += ALPHABET[zahl]
    return text
#7: Erzeugen einer Textfile, welche den angegebenen String enthaelt.
def save_textfile(text):
    print("Unter welchem Namen soll der text gespeichert werden?")
    name = input()
    fobj_out = open("Texte/"+name + ".txt","w")
	#zeilenanzahl = int(len(text)/8)
    for i in range(int(len(text)/32)+1):
        for k in range(4):
            for j in range(8):
                try:
                    fobj_out.write(text[32*i+8*k+j].upper())
                except IndexError:
                    fobj_out.write(' ') #eigentlich: exit loop
            fobj_out.write(' ')
        fobj_out.write('\n')
    fobj_out.close()
####################################################################################
