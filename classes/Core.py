from .Script import Script
import os, idlelib, sys, threading

class Core:
    def __init__(self,rootdir):
        self.rootdir = rootdir
        self.scripts = {}
        self.loadScripts()
    
    def loadScripts(self):
        path = os.path.join(self.rootdir, 'scripts')
        for name in os.listdir(path):
            f = os.path.join(path,name)
            if (os.path.isdir(f)):
                self.addScript(name)

    def addScript(self,name):
        self.scripts[name] = Script(os.path.join(self.rootdir,'scripts',name))

    def openScript(self,name):
        sys.argv = ['-e',os.path.join(self.scripts[name].path,'script.py')]
        t = threading.Thread(target=idlelib.PyShell.main)
        t.start()

    def runScript(self,name):
         self.scripts[name].run()
