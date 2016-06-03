import os
class TestCase:    
    def __init__(self,inpath):
        self.name = os.path.split(inpath)[-1][5:-4]
        self.inPath = inpath
        self.outPath = os.path.join(os.sep.join(inpath.split(os.sep)[:-2]),'output','output'+self.name+'.txt')
        self.status = 0
        self.data = ''

    def getInPath(self):
        return self.inPath

    def getOutPath(self):
        return self.outPath

    def setStatus(self,statusCode):
        self.status = statusCode

    def getStatus(self):
        if (self.status == 0):
            return 'WAITING'
        elif (self.status == 1):
            return 'PASSED'
        elif (self.status == 2):
            return 'FAILED'
        elif (self.status == 3):
            return 'ERROR'
        else:
            return 'UNKNOWN STATUS CODE'
