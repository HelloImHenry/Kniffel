from tkinter import *
from tkinter import filedialog
import os
sizeX = 500
path = os.path.realpath(__file__)
saveWindow = Tk()
saveWindow.geometry("200x200")
root = Tk()
scrollbar = Scrollbar(root, orient = HORIZONTAL)
scrollbar.pack(side = TOP, fill=X)
root.geometry("500x500")
cv = Canvas(root, width=500,height=500)
#path = filedialog.asksaveasfile(filetypes=[("JSON-File",".json"), ("Textdokument",".txt")], initialdir = "D:\PyCharm\Kniffel")
#file = open(path, 'r')
root.mainloop()