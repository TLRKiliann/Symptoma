#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


class Application(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='deep sky blue', padx=20, pady=20, relief=GROOVE)
        self.master.title('Symptoma - Developed by ko@l@tr33 - 2020')

        # ScrollCanvas limite de la zone à parcourir avec la barre
        self.can = Canvas(self, width=1250, height=800, bg='aquamarine')
        self.frame = Frame(self.can)

        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW, tags="self.frame")
        # Insertion of picture
        self.photo = PhotoImage(file='./picgif/bg.png')
        self.item = self.can.create_image(625, 400, image=self.photo)
        # Insertion of text
        self.can.create_text(300, 100, anchor=CENTER, 
            text="Text below to read search", font=('Times New Roman', 18, 'bold'), fill='navy')
        self.can.create_text(980, 540, anchor=NE, text="ko@l@tr33",
            font=('Times', 12), fill='navy')
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)

        self.top = Frame(self.can, bg='aquamarine')
        self.bottom = Frame(self.can)
        self.top.pack(side=TOP, pady=2)
        self.bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

        def searchExpress():
            """
            To read into right file
            """
            mot = self.regexpi_var.get()
            if (mot == str("syndrome extrapyramidal")) or (mot == str("extrapyramidal syndrom")):
                importationExtrapy()
                print("Ok, ici c'est extra...pyramidale")
            elif (mot == str("syndrome neuroleptique")) or (mot == str("neuroleptic syndrom")):
                importationNeuro()
                print("Ok, là c'est neuro...")
            elif (mot == str("syndrome anticholinergique")) or (mot == str("anticholinergic syndrom")):
                importationAnticho()
                print("Ok, ici c'est anticho...")
            elif (mot == str("syndrome serotoninergique")) or (mot == str("serotoninergic syndrom")):
                importationSeroton()
                print("Ok, ici c'est serotoni...")                
            else:
                print("Ici, c'est la merde...")

        # Display text in textbox from medifile files
        def importationNeuro():
            try:
                if os.path.getsize('./medifile/neuro_syndrom.txt'):
                    print("+ File 'neuro_syndrom.txt' exist (read)!")
                    with open('./medifile/neuro_syndrom.txt', 'r') as textfile1:
                        lines = textfile1.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'neuro_syndrom.txt' does not exist !", outnote)

        # Display text in textbox from medifile files
        def importationExtrapy():
            try:
                if os.path.getsize('./medifile/extrapy_syndrom.txt'):
                    print("+ File 'extrapy_syndrom.txt' exist (read)!")
                    with open('./medifile/extrapy_syndrom.txt', 'r') as textfile2:
                        lines = textfile2.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote2:
                print("+ Sorry, file 'extrapy_syndrom.txt' does not exist !", outnote2)

        # Display text in textbox from medifile files
        def importationAnticho():
            try:
                if os.path.getsize('./medifile/anticho_syndrom.txt'):
                    print("+ File 'anticho_syndrom.txt' exist (read)!")
                    with open('./medifile/anticho_syndrom.txt', 'r') as textfile3:
                        lines = textfile3.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote3:
                print("+ Sorry, file 'anticho_syndrom.txt' does not exist !", outnote3)

        # Display text in textbox from medifile files
        def importationSeroton():
            try:
                if os.path.getsize('./medifile/seroton_syndrom.txt'):
                    print("+ File 'seroton_syndrom.txt' exist (read)!")
                    with open('./medifile/seroton_syndrom.txt', 'r') as textfile4:
                        lines = textfile4.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote4:
                print("+ Sorry, file 'seroton_syndrom.txt' does not exist !", outnote4)

        # Text entry
        self.regexpi_var = StringVar()
        self.reachDate = Entry(self.can, textvariable=self.regexpi_var, width=40)
        self.regexpi_var.set("Enter a syndrom here")
        self.reachDate.pack(in_=self.top, side=LEFT, padx=10, pady=20)

        # Button to search text entry
        self.buttonSearch = Button(self.can, text='Search', width=8, bd=3,
            fg='navy', bg='cyan', highlightbackground='darkblue',
            activebackground='light blue', command=searchExpress)
        self.buttonSearch.pack(in_=self.top, side=LEFT, padx=10, pady=20)

        def upDateAll():
            self.master.destroy()
            subprocess.call('./neuro_psy.py')

        # Button to update
        self.buttonSearch = Button(self.can, text='Refresh', width=8, bd=3,
            fg='navy', bg='cyan', highlightbackground='darkblue',
            activeforeground='yellow',
            activebackground='light blue', command=upDateAll)
        self.buttonSearch.pack(in_=self.top, side=LEFT, padx=10, pady=20)

        # Button to quit
        self.buttonSearch = Button(self.can, text='Quit', width=8, bd=3,
            fg='white', bg='DodgerBlue2', highlightbackground='darkblue',
            activeforeground='red',
            activebackground='light blue', command=quit)
        self.buttonSearch.pack(in_=self.top, side=LEFT, padx=10, pady=20)

        # TextBox
        self.textBox=Text(self.can, height=20, width=80, font=18, relief=SUNKEN)
        self.textBox.pack(padx=100, pady=50)

        self.pack()

if __name__=='__main__':
    app = Application()
    app.mainloop()
