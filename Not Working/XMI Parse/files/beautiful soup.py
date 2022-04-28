from bs4 import BeautifulSoup
import re


with open('C:\\Users\\vanderweck\\PycharmProjects\\Not Working\\XMI Parse\\Models\\ID2.xmi', 'r') as ID4:
    soup = BeautifulSoup(ID4, features="xml")
    #text = str(soup.findAll(text=True)).replace("\\n", " ")

fehlerID = soup.find("TAG_01_Fehler_ID")
fehlerbeschreibung = soup.find("TAG_02_Fehlerbeschreibung")

Fehlermeldung = [fehlerID, fehlerbeschreibung]

print(Fehlermeldung)
