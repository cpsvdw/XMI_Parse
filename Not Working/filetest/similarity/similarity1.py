# import the enchant module
import enchant
import re
import pandas as pd
import numpy as np

string1 = f"C:/Users/vanderweck/PycharmProjects/filetest/files/XMI_1.xmi"
string2 = f"C:/Users/vanderweck/PycharmProjects/filetest/files/XMI_2.xmi"


# the Levenshtein distance between
# string1 and string2


def sim1():
    a = enchant.utils.levenshtein(string1, string2)
    b = len(string1)
    c = len(string2)
    d = (b / a) * 100
    print(a)


print(sim1())
