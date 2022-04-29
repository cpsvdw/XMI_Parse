import PyXMI

filepath = 'C:\\Users\\vanderweck\\PycharmProjects\\Not Working\\XMI Parse\\Models\\ID2.xmi'
model = PyXMI.stateMachine(filepath)
dom = model.dom
# get the dom and we can traverse it.


# Let's try something else. Create a society of class
classes = PyXMI.classSociety(file_name=filepath)
print(classes)
from IPython import embed

embed()
