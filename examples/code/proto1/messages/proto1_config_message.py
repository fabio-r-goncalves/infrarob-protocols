import json
class Config:

    def __init__(self):
        pass

    def __init__(self, datasinkIP, datasinkPort):
        self.datasinkIP = datasinkIP
        self.datasinkPort = datasinkPort

    def __init__(self, datasinkIP, datasinkPort, method, period):
        self.datasinkIP = datasinkIP
        self.datasinkPort = datasinkPort
        self.setSendingMethod(method, period)
    
    def setDataSinkIP(self, datasinkIP):
        self.datasinkIP = datasinkIP
    
    def setDataSinkPort(self, datasinkPort):
        self.datasinkPort = datasinkPort

    def setSendingMethod(self, method, period):
        self.method = method
        self.period = period


    def getDataSinkIP(self):
        return self.datasinkIP
    
    def getDataSinkPort(self):
        return self.datasinkPort
    
    def getSendingMethod(self):
        return {"method":self.method, "period":self.period}

    
    def configToJson(self):
        return {
            "datasinkIP":self.datasinkIP,
            "datasinkPort": self.datasinkPort,
            "sendingMethod": self.getSendingMethod()
        }