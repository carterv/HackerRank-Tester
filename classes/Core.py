from .Project import Project
import os, sys, subprocess, shutil

class Core:
    def __init__(self,rootdir):
        self.rootdir = rootdir
        self.projects = {}
        self.loadProjects()
    
    def loadProjects(self):
        path = os.path.join(self.rootdir, 'projects')
        for name in os.listdir(path):
            f = os.path.join(path,name)
            if (os.path.isdir(f)):
                self.addProject(name)

    def addProject(self,name):
        self.projects[name] = Project(os.path.join(self.rootdir,'projects',name))

    def openProject(self,name):
        args = ['python',os.path.join(sys.exec_prefix,'Lib','idlelib','idle.py'),'-e',os.path.join(self.projects[name].path,'script.py')]
        subprocess.Popen(args,close_fds=True,creationflags=0x00000008) #DETACHED_PROCESS creation flag
    
    def deleteProject(self,name):
        path = self.projects[name].path
        shutil.rmtree(path)
        del self.projects[name]

    def runProject(self,name):
         self.projects[name].run()

    def getProjects(self):
        return self.projects.keys()

    def getProject(self,name):
        return self.projects[name]
