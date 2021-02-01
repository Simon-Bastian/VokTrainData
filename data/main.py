from tkinter import Tk, simpledialog, messagebox
import random

print('Vokabel Trainer by ItzSimmi, Verion 0.1 Beta')
root = Tk()
root.withdraw()
abfrage = {}

while True:
    aufgabe = simpledialog.askstring('Aufgabe', '1: Abfrage   2: Eingeben')
    if aufgabe == '1':
        while True:
            line = random()

    elif aufgabe == '2':
        while True:
            file = open("vok.txt","w")
            neues_deutsch = simpledialog.askstring('Deutsch', 'Wie ist das Deutsche Wort?')
            print(neues_deutsch)
            file.write(neues_deutsch + ('/'))
            neues_fremdsprache = simpledialog.askstring('Frendsprache', 'Wie ist das Wort in der Fremdsprache?')
            print(neues_fremdsprache)
            file.write(neues_fremdsprache + ('\n')
        break