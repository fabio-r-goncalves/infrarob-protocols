

class Proto1Message:
    version = 1.0

    
    def __init__(self, timesamp, seqnumber, status):
        self.timestamp = timesamp
        self.seqnumber = seqnumber
        self.status = status
        self.request = ""
        self.objects = ""
        self.config = ""

    def getTimestam(self):
            return self.timestamp
    
    def getSeqNumber(self):
            return self.seqnumber

    def getStatus(self):
            return self.status
    
    def setRequest(self, request):
        self.request = request

    def setObjects(self, objects):
        self.objects = objects    
            
    def getObjects(self):
        return self.objects
    
    def getRequest(self):
        return self.request
    
    def setConfig(self, config):
        self.config = config
    
    def getConfig(self):
         return self.config
    
    def messageToJson(self):
         
         return {
              "version": self.version,
              "timesamp": self.timestamp,
              "seqnumber": self.seqnumber,
              "status": self.seqnumber,
              "config": self.config,
              "objects": self.objects,
              "request": self.request
         }