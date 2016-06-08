from tkinter import *
from tkinter.ttk import *

class MainWindow(Frame):
    def __init__(self,core,master=None):
        Frame.__init__(self,master)
        self.core = core
        self.master.resizable(0,0)
        self.master.geometry('600x420')
        self.pack(expand=False)
        self.widgets = {}
        self.createWidgets()
        self.populateProjects()

    def createWidgets(self):
        #Project pane widgets
        ft = Frame(self.master)
        ft.pack(side=TOP,fill=X)

        f1 = Frame(ft)
        f1.pack(side=TOP,fill=X)
        self.widgets['PLabel'] = Label(f1,text='Projects',justify=LEFT)
        self.widgets['PLabel'].pack(side=LEFT,expand=False)
        
        f2 = Frame(ft)
        f2.pack(side=TOP,expand=False,fill=X)
        self.widgets['PScroll'] = Scrollbar(f2)
        self.widgets['PScroll'].pack(side=RIGHT,fill=Y)
        self.widgets['Projects'] = Listbox(f2,yscrollcommand=self.widgets['PScroll'].set)
        self.widgets['Projects'].pack(side=TOP,fill=X)
        self.widgets['Projects'].bind('<<ListboxSelect>>',self.loadTests)
        
        f3 = Frame(ft)
        f3.pack(side=TOP,expand=False,fill=X)
        self.widgets['PNew'] = Button(f3,text='New')
        self.widgets['PNew'].pack(side=LEFT,expand=False) 
        self.widgets['PDelete'] = Button(f3,text='Delete')
        self.widgets['PDelete'].pack(side=LEFT,expand=False)
        self.widgets['PAdd'] = Button(f3,text='Add')
        self.widgets['PAdd'].pack(side=LEFT,expand=False)
        self.widgets['POpen'] = Button(f3,text='Open',command=self.openProject)
        self.widgets['POpen'].pack(side=LEFT,expand=False)

        #Test Case Pane Widgets
        fb = Frame(self.master)
        fb.pack(side=BOTTOM,expand=True,fill=X)
        
        f4 = Frame(fb)
        f4.pack(side=TOP,expand=True,fill=X)
        self.widgets['TLabel'] = Label(f4,text='Test Cases',justify=LEFT)
        self.widgets['TLabel'].pack(side=LEFT,expand=False)

        f5 = Frame(fb)
        f5.pack(side=TOP,expand=False,fill=X)
        self.widgets['TScroll'] = Scrollbar(f5)
        self.widgets['TScroll'].pack(side=RIGHT,fill=Y)
        self.widgets['TestCases'] = Listbox(f5,yscrollcommand=self.widgets['TScroll'].set)
        self.widgets['TestCases'].pack(side=TOP,expand=True,fill=X)

        f6 = Frame(fb)
        f6.pack(side=TOP,expand=False,fill=X)
        self.widgets['TRun'] = Button(f6,text='Run')
        self.widgets['TRun'].pack(side=LEFT,expand=False)
        self.widgets['TLoad'] = Button(f6,text='Load')
        self.widgets['TLoad'].pack(side=LEFT,expand=False)
        self.widgets['TOptions'] = Button(f6,text='Options')
        self.widgets['TOptions'].pack(side=LEFT,expand=False)

    def populateProjects(self):
        projects = list(self.core.getScripts())
        projects.sort()
        w = self.widgets['Projects']
        for p in projects:
            w.insert(w.size(),p)

    def loadTests(self,event):
        try:
            w = event.widget
            name = w.get(int(w.curselection()[0]))
            tests = [t.name for t in self.core.getScript(name).testCases]
            w = self.widgets['TestCases']
            w.delete(0,w.size())
            for t in tests:
                w.insert(w.size(),t)
        except:
            pass

    def openProject(self):
        try:
            w = self.widgets['Projects']
            name = w.get(int(w.curselection()[0]))
            self.core.openScript(name)
        except:
            pass
