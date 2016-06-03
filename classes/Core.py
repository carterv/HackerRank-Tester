from .Script import Script
import os

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

    def openScript(self):
        pass

    def runScript(self,name):
         self.scripts[name].run()
