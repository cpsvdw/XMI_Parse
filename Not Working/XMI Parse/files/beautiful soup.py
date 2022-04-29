from bs4 import BeautifulSoup as bs

id2 = []
fehlermeldung = []
with open('C:\\Users\\vanderweck\\PycharmProjects\\Not Working\\XMI Parse\\Models\\ID2.xmi', 'r') as file:
    id2 = file.readlines()
id2 = "".join(id2)
bs_content = bs(id2, features="xml")

# fehlerID = bs_content.find_all("TAG_01_Fehler_ID")
# fehlerbeschreibung = bs_content.find_all("TAG_02_Fehlerbeschreibung")
# fehlermeldung = [fehlerID, fehlerbeschreibung]
fehlermeldung = bs_content.find_all("MA_Simon_Library_colon03_Fehler_Label_colon02_Stereotype:Fehler_Label").get(
    "TAG_01_Fehler_ID")

print(fehlermeldung)
