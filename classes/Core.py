from .Script import Script
import os, sys, subprocess

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
        args = ['python',os.path.join(sys.exec_prefix,'Lib','idlelib','idle.py'),'-e',os.path.join(self.scripts[name].path,'script.py')]
        subprocess.Popen(args,close_fds=True,creationflags=0x00000008) #DETACHED_PROCESS creation flag

    def runScript(self,name):
         self.scripts[name].run()
