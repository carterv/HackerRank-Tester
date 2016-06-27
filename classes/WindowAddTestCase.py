from tkinter import *
from tkinter.ttk import *

class WindowAddTestCase(Frame):
    def __init__(self,core,projectname,master=None):
        self.master = Toplevel(master)
        self.master
        self.core = core
        self.project = core.getProject(projectname)
        
        self.master.title('New test case for ' + projectname)
        self.master.resizable(0,0)
        self.master.focus_force()
        self.master.bind('<Control-w>',lambda e:self.master.destroy())
        
        self.widgets = {}
        self.createWidgets()

    def createWidgets(self):
        ftop = Frame(self.master)
        ftop.pack(side=TOP,fill=X)

        f1 = Frame(ftop)
        f1.pack(side=LEFT,expand=False)
        self.widgets['ILabel'] = Label(f1,text='Input',justify=LEFT)
        self.widgets['ILabel'].pack(side=TOP,fill=X)

        f2 = Frame(f1)
        f2.pack(side=TOP,expand=False)
        self.widgets['IScrollY'] = Scrollbar(f2)
        self.widgets['IScrollY'].pack(side=RIGHT,fill=Y,pady=1)
        self.widgets['IScrollX'] = Scrollbar(f2,orient=HORIZONTAL)
        self.widgets['IScrollX'].pack(side=BOTTOM,fill=X,padx=1)
        self.widgets['IText'] = Text(f2,xscrollcommand=self.widgets['IScrollX'].set,yscrollcommand=self.widgets['IScrollY'].set)
        self.widgets['IText'].pack(side=TOP,padx=1,pady=1)

        f3 = Frame(ftop)
        f3.pack(side=RIGHT,expand=False)
        self.widgets['OLabel'] = Label(f3,text='Output',justify=LEFT)
        self.widgets['OLabel'].pack(side=TOP,fill=X)

        f4 = Frame(f3)
        f4.pack(side=TOP,expand=False)
        self.widgets['OScrollY'] = Scrollbar(f4)
        self.widgets['OScrollY'].pack(side=RIGHT,fill=Y,pady=1)
        self.widgets['OScrollX'] = Scrollbar(f4,orient=HORIZONTAL)
        self.widgets['OScrollX'].pack(side=BOTTOM,fill=X,padx=1)
        self.widgets['OText'] = Text(f4,xscrollcommand=self.widgets['OScrollX'].set,yscrollcommand=self.widgets['OScrollY'].set)
        self.widgets['OText'].pack(side=TOP,padx=1,pady=1)

        fbottom = Frame(self.master)
        fbottom.pack(side=BOTTOM,expand=False,fill=X)
        self.widgets['Create'] = Button(fbottom,text='Create',command=self.createProject)
        self.widgets['Create'].pack(side=LEFT)
        self.widgets['Cancel'] = Button(fbottom,text='Cancel',command=self.cancel)
        self.widgets['Cancel'].pack(side=LEFT)

        createProject = lambda e:self.createProject()

        self.widgets['IText'].focus_set()
        self.widgets['IText'].bind('<Return>',createProject)
        self.widgets['IText'].bind('<Tab>',self.changeFocus)
        self.widgets['OText'].bind('<Return>',createProject)
        self.widgets['OText'].bind('<Tab>',self.changeFocus)

    def createProject(self):
        self.project.createTestCase(self.widgets['IText'].get('0.0'),self.widgets['OText'].get('0.0'))
        self.master.destroy()

    def cancel(self):
        self.master.destroy()

    def changeFocus(self,event):
        event.widget.tk_focusNext().focus()
        return 'break'
