from tkinter import *
from tkinter.ttk import *

class WindowAddProject(Toplevel):
    def __init__(self,master=None):
        self.master = Toplevel(master)
        self.master.resizable(0,0)
        self.widgets = {}
        self.createWidgets()

    def createWidgets(self):
        ftop = Frame(self.master)
        ftop.pack(side=TOP,fill=X)

        f1 = Frame(ftop)
        f1.pack(side=TOP,expand=False,fill=X)
        self.widgets['NLabel'] = Label(f1,text='Project Name',justify=LEFT)
        self.widgets['NLabel'].pack(side=TOP,fill=X)

        f2 = Frame(ftop)
        f2.pack(side=TOP,expand=False,fill=X)
        self.widgets['NEntry'] = Entry(f2)
        self.widgets['NEntry'].pack(side=TOP,fill=X)
        
        #Checkbox, with Label (Open this project in IDLE after creation)
        #Button (OK), Button (Cancel)
