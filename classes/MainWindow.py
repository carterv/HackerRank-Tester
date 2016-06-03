import tkinter as tk

class MainWindow(tk.Frame):
    def __init__(self,core,master=None):
        tk.Frame.__init__(self,master)
        self.core = core
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        pass
