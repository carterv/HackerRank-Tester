from tkinter import *
from tkinter.ttk import *

class WindowAddProject(Toplevel):
    def __init__(self,core,master=None):
        self.master = Toplevel(master)
        self.core = core
        self.master.title('New Project')
        self.master.resizable(0,0)
        self.master.geometry('300x90')
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
        self.widgets['NEntry'].pack(side=TOP,fill=X,padx=1,pady=1)

        f3 = Frame(ftop)
        f3.pack(side=TOP,expand=False,fill=X)
        self.widgets['Checkvar'] = IntVar()
        self.widgets['Checkbutton'] = Checkbutton(f3,text='Open in IDLE',variable=self.widgets['Checkvar'])
        self.widgets['Checkbutton'].pack(side=TOP,fill=X,padx=1,pady=1)

        f4 = Frame(ftop)
        f4.pack(side=TOP,expand=False,fill=X)

        f5 = Frame(ftop)
        f5.pack(side=TOP,expand=False,fill=X)
        self.widgets['Create'] = Button(f5,text='Create',command=self.createProject)
        self.widgets['Create'].pack(side=LEFT,expand=False,padx=1,pady=1)
        self.widgets['Cancel'] = Button(f5,text='Cancel',command=self.cancel)
        self.widgets['Cancel'].pack(side=LEFT,expand=False,padx=1,pady=1)

    def createProject(self):
        name = self.widgets['NEntry'].get()
        if (name == '' or not self.verify(name)):
            return
        self.core.addProject(name)
        self.master.destroy()
        if (self.widgets['Checkvar'].get()):
            self.core.openProject(name)

    def cancel(self):
        pass

    def verify(self,name):
        valid = 'abcdefghijklmnopqrstuvwxyz0123456789 '
        sname = set(name)
        for c in sname:
            if not c in valid:
                return False
        return True
