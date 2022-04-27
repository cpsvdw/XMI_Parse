from bs4 import BeautifulSoup
import re

with open("C:\Users/vanderweck\OneDrive - consultens Professional Services GmbH/Dokumente Simon/99_Masterarbeit/80_Demonstrator/04_Modelle/XMI/ID4.xmi") as ma:
    soup = BeautifulSoup(ma)

soup = BeautifulSoup(markup, "xml")

file = open(
    "C:\Users/vanderweck\OneDrive - consultens Professional Services GmbH/Dokumente Simon/99_Masterarbeit/80_Demonstrator/04_Modelle/XMI/ID4.xmi",
    "r")
contents = file.read()

soup = BeautifulSoup(contents, "lxml")
text = str(soup.findAll(text=True)).replace("\\n", " ")

fehlerID = soup.find("TAG_01_Fehler_ID")
fehlerbeschreibung = soup.find("TAG_02_Fehlerbeschreibung")

Fehlermeldung = []


