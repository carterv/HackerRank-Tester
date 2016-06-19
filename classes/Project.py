from .TestCase import TestCase
import os, subprocess, time

class Project:
    def __init__(self,path):
        self.name = path.split(os.sep)[-1]
        self.path = path
        self.testCases = []
        folders = ['','tests'+os.sep+'input','tests'+os.sep+'output']
        for f in folders:
            p = os.path.join(self.path,f)
            if (not os.path.exists(p)):
                os.makedirs(p)
        path = os.path.join(self.path,'script.py')
        if (not os.path.exists(path)):
            open(path,"w+")
        self.loadTestCases()

    def loadTestCases(self):
        for f in os.listdir(os.path.join(self.path,'tests','input')):
            ip = os.path.join(self.path,'tests','input',f)
            op = os.path.join(self.path,'tests','output','output'+f[5:])
            if (os.path.isfile(ip) and os.path.isfile(op)):
                self.addTestCase(ip)

    def addTestCase(self,path):
        self.testCases.append(TestCase(path))

    def run(self):
        for test in self.testCases:
            child = subprocess.Popen(['python',os.path.join(self.path,'script.py')],stdin=open(test.getInPath(),'r'),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            infile = open(test.getInPath(),'r')
            child.wait()
            results = []
            while True:
                line = child.stdout.readline().decode('utf-8').strip()
                if (line != ''):
                    results.append(line)
                else:
                    break
            results = "\n".join(results)
            errors = child.stderr.read().decode('utf-8').strip()
            expected = open(test.getOutPath(),'r').read().strip()
            if (not errors == ''):
                test.setStatus(3)
                test.data = errors
            elif (not results == expected):
                test.setStatus(2)
                test.data = results
            else:
                test.setStatus(1)
