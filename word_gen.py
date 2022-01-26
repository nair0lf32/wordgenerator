import itertools
import tkinter
from tkinter import *

info = '''

######################################################
           made_By:   florian_E.          
           
.-..-..---..-..---. .----..-.   .---.
| .` || | || || |-< | || || |__ | |- 
`-'`-'`-^-'`-'`-'`-'`----'`----'`-'  
                                                                  
######################################################

       '''
print(info)

print("")

alphabet_min = "abcdefghijklmopqrstuvwxyz"
alphatbet_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeric = "0123456789"
special = " éà@ç-\/:#{}[]()'&*"

main_window = Tk()
main_window.title = "word_gen"
main_window.geometry("300x300")

def generate(longueur=3, liste= special):
    words = itertools.permutations(liste, longueur)
    for x in liste:
        yield x
        print(x)


lab = Label(main_window, text = "Générateur de wordlist" , fg = "green")
lab.pack()

b = Button(main_window, text ="Générer", bg = "red", command=generate)
b.pack(side = tkinter.BOTTOM)

main_window.mainloop()




