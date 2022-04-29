from xml.etree import ElementTree as ET

parser = ET.iterparse('C:\\Users\\vanderweck\\PycharmProjects\\Not Working\\XMI Parse\\Models\\ID2.xmi')

for event, element in parser:
    print(element.tag)
