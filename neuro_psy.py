#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


class Application(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='grey22', padx=20, pady=20, relief=GROOVE)
        self.master.title('ANGEL-VISION - Developed by ko@l@tr33 - 2020')

        # ScrollCanvas limite de la zone à parcourir avec la barre
        self.can = Canvas(self, width=1250, height=800, bg='grey18')
        self.frame = Frame(self.can)

        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW, tags="self.frame")
        # Insertion of picture
        self.photo = PhotoImage(file='./picgif/bg.png')
        self.item = self.can.create_image(625, 400, image=self.photo)
        # Insertion of text
        self.can.create_text(625, 420, anchor=CENTER, 
            text="Hello",
            font=('Times New Roman', 18, 'bold'), fill='turquoise')
        self.can.create_text(1240, 770, anchor=NE, text="ko@l@tr33",
            font=('Times', 12), fill='turquoise')
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)

        # TextBox
        self.textBox=Text(self.can, height=20, width=80, font=18, relief=SUNKEN)
        self.textBox.pack(padx=100, pady=100)

        # Display text in textbox from medifile files
        def importationFile(fichier, encodage="Utf-8"):
            file = open(fichier, 'r', encoding=encodage)
            content = file.readlines()
            file.close()
            for li in content:
                self.textBox.insert(END, li)
        try:
            importationFile('./medifile/neuro_syndrom.txt',
                encodage="Utf-8")
        except FileNotFoundError as filereach:
            print("File neuro_syndrom.txt does not exist", filereach)

        self.pack()

if __name__=='__main__':
    app = Application()
    app.mainloop()
