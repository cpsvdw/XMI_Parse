from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

id2 = []
fehlermeldung = []
with open('C:\\Users\\vanderweck\\PycharmProjects\\Not Working\\XMI Parse\\Models\\ID2.xmi', 'r') as file:
    id2 = requests.get(file).content
    soup = bs(id2, "lxml")

    texts = str(soup.findAll(text=True)).replace('\\n', '')

    fehlerID = []
    fehlerbeschreibung = []

    while True:
        try:
            fehlerID.append(" ".join(child.find('TAG_01_Fehler_ID')))
        except:
            fehlerID.append(" ")

        try:
            fehlerbeschreibung.append(" ".join(child.find('TAG_02_Fehlerbeschreibung')))
        except:
            fehlerbeschreibung.append(" ")

data = []
data = pd.DataFrame({"fehlerID": fehlerID, "fehlerbeschreibung": fehlerbeschreibung})
print(data)
