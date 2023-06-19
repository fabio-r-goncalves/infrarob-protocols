

class Proto1Objects:

    def __init__(self):
        pass

    def __init__(
            self, 
            objectID, 
            speed,
            speedConfidence,
            longAcc,
            longAccConfidence,
            heading,
            headingConfidence,
            lat,
            long,
            positionConfidence,
            length,
            lengthConfidence,
            lane,
            laneConfidence):
        self.objectID = objectID
        self.speed = speed,
        self.speedConfidence = speedConfidence
        self.longAcc = longAcc
        self.longAccConfidence = longAccConfidence
        self.heading = heading
        self.headingConfidence = headingConfidence
        self.lat = lat
        self.long = long
        self.positionConfidence = positionConfidence
        self.length = length
        self.lengthConfidence = lengthConfidence
        self.lane = lane
        self.laneConfidence = laneConfidence
        


    def getObjectID(self):
        return self.objectID
    def getSpeed(self):
        return self.speed
    def getSpeedConfidence(self):
        return self.speedConfidence
    def getLongAcc(self):
        return self.longAcc
    def getLongAccConfidence(self):
        return self.longAccConfidence
    def getHeading(self):
        return self.heading
    def getHeadingConfidence(self):
        return self.headingConfidence
    def getLat(self):
        return self.lat
    def getLong(self):
        return self.long
    def getPositionConfidence(self):
        return self.positionConfidence
    def getLength(self):
        return self.length
    def getLengthConfidence(self):
        return self.lengthConfidence
    def getLane(self):
        return self.lane
    def getLaneConfidence(self):
        return self.laneConfidence
    
    def ObjectsToJson(self):
        return {
            "objectID": self.objectID,
            "speed": self.speed,
            "speedConfidence": self.speedConfidence,
            "longAcc": self.longAcc,
            "longAccConfidence": self.longAccConfidence,
            "heading": self.heading,
            "headingConfidence": self.headingConfidence,
            "lat": self.lat,
            "long": self.long,
            "positionConfidence": self.positionConfidence,
            "lengthConfidence": self.lengthConfidence,
            "lane": self.lane,
            "laneConfidence": self.laneConfidence
        }