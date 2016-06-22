from tkinter import *
from tkinter.ttk import *
from .WindowAddProject import WindowAddProject
from .WindowAddTestCase import WindowAddTestCase

class WindowMain(Frame):
    def __init__(self,core,master=None):
        Frame.__init__(self,master)
        self.core = core
        self.curselection = None
        self.master.resizable(0,0)
        self.master.geometry('600x420')
        self.pack(expand=False)
        self.widgets = {}
        self.createWidgets()
        self.populateProjects()

    def createWidgets(self):
        #Project pane widgets
        ftop = Frame(self.master)
        ftop.pack(side=TOP,fill=X)

        f1 = Frame(ftop)
        f1.pack(side=TOP,fill=X)
        self.widgets['PLabel'] = Label(f1,text='Projects',justify=LEFT)
        self.widgets['PLabel'].pack(side=LEFT,expand=False)
        
        f2 = Frame(ftop)
        f2.pack(side=TOP,expand=False,fill=X)
        self.widgets['PScroll'] = Scrollbar(f2)
        self.widgets['PScroll'].pack(side=RIGHT,fill=Y,pady=1)
        self.widgets['Projects'] = Listbox(f2,yscrollcommand=self.widgets['PScroll'].set)
        self.widgets['Projects'].pack(side=TOP,fill=X,padx=1,pady=1)
        self.widgets['Projects'].bind('<<ListboxSelect>>',self.loadTests)
        
        f3 = Frame(ftop)
        f3.pack(side=TOP,expand=False,fill=X)
        self.widgets['POpen'] = Button(f3,text='Open',command=self.openProject)
        self.widgets['POpen'].pack(side=LEFT,expand=False)
        self.widgets['PNew'] = Button(f3,text='New',command=self.newProject)
        self.widgets['PNew'].pack(side=LEFT,expand=False)
        self.widgets['PDelete'] = Button(f3,text='Delete',command=self.deleteProject)
        self.widgets['PDelete'].pack(side=LEFT,expand=False)

        #Test Case Pane Widgets
        fbottom = Frame(self.master)
        fbottom.pack(side=BOTTOM,expand=True,fill=X)
        
        f4 = Frame(fbottom)
        f4.pack(side=TOP,expand=True,fill=X)
        self.widgets['TLabel'] = Label(f4,text='Test Cases',justify=LEFT)
        self.widgets['TLabel'].pack(side=LEFT,expand=False)

        f5 = Frame(fbottom)
        f5.pack(side=TOP,expand=False,fill=X)
        self.widgets['TScroll'] = Scrollbar(f5)
        self.widgets['TScroll'].pack(side=RIGHT,fill=Y,pady=1)
        self.widgets['TestCases'] = Listbox(f5,yscrollcommand=self.widgets['TScroll'].set)
        self.widgets['TestCases'].pack(side=TOP,fill=X,padx=1,pady=1)

        f6 = Frame(fbottom)
        f6.pack(side=TOP,expand=False,fill=X)
        self.widgets['TRun'] = Button(f6,text='Run',command=self.runTests)
        self.widgets['TRun'].pack(side=LEFT,expand=False)
        self.widgets['TNew'] = Button(f6,text='New',command=lambda:self.newTest() if self.curselection else None)
        self.widgets['TNew'].pack(side=LEFT,expand=False)

    def populateProjects(self):
        w = self.widgets['Projects']
        w.delete(0,w.size())
        projects = list(self.core.getProjects())
        projects.sort()
        for p in projects:
            w.insert(w.size(),p)

    def loadTests(self,event):
        try:
            w = event.widget
            name = w.get(int(w.curselection()[0]))
            self.curselection = name
            self.reloadTests(name)
        except:
            self.curselection = None

    def reloadTests(self,name):
        tests = [t.name + ' ' + t.getStatus() for t in self.core.getProject(name).testCases]
        w = self.widgets['TestCases']
        w.delete(0,w.size())
        for t in tests:
            w.insert(w.size(),t)

    def openProject(self):
        w = self.widgets['Projects']
        name = self.curselection
        self.core.openProject(name)

    def newProject(self):
        w = WindowAddProject(self.core,self)
        self.master.wait_window(w.master)
        self.populateProjects()

    def deleteProject(self):
        w = self.widgets['Projects']
        name = self.curselection
        self.core.deleteProject(name)
        self.populateProjects()

    def runTests(self):
        w = self.widgets['Projects']
        name = self.curselection
        self.core.runProject(name)
        self.reloadTests(name)

    def newTest(self):
        nw = self.widgets['Projects']
        name = self.curselection
        
        w = WindowAddTestCase(self.core,name,self)
        self.master.wait_window(w.master)
        
        self.reloadTests(name)
