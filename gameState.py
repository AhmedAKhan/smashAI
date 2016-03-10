import struct;

class gameState:
    def __init__(self):
        self.hexToState = {};
        self.state = {};
    def createEmptyState(self):
        self.state = {
            "p1":{
                "action":0,
                "actionCounter":0,
                "actionFrame":0,
                "invulnerable":False,
                "hitlagFramesLeft":0,
                "hitStunFramesLeft":0,
                "isChargingSmash":False,
                "jumpsRemaining":0,
                "isOnGround":True,
                "speedAirX":0,
                "speedAirY":0,
                "speedXAttack":0,
                "speedYAttack":0,
                "speedGroundX":0,
                "damage":100,
                "stocks":4,
                "facingLeft":True,
                "character":0,
                "x":0,
                "y":0
            },
            "p2":{
                "action":0,
                "actionCounter":0,
                "actionFrame":0,
                "invulnerable":False,
                "hitlagFramesLeft":0,
                "hitStunFramesLeft":0,
                "isChargingSmash":False,
                "jumpsRemaining":0,
                "isOnGround":True,
                "speedAirX":0,
                "speedAirY":0,
                "speedXAttack":0,
                "speedYAttack":0,
                "speedGroundX":0,
                "damage":100,
                "stocks":4,
                "facingLeft":True,
                "character":0,
                "x":0,
                "y":0,
                "cursorX":0,
                "cursorY":0
            },
            "frame":0,
            "menuState":0,
            "stage":0
        };

    def adjustValue(self, region, value):
        def convertToInt(curVal, shiftVal): return int(curVal, 16) >> shiftVal;
        def convertToBool(curVal, shiftVal): return bool(int(curVal, 16) >> shiftVal);
        def convertToFloat(curVal): return struct.unpack('f',struct.pack('I',int(curVal,16)));
        value = value[0:-1];
        inputAddressList = region.split(" ");
        baseInt = int(inputAddressList[0],16);
        if(len(inputAddressList) == 1): ## its a direct pointer
            self.state[self.hexToState[region]] = value;
        else:
            ## TODO
            t = type(self.state[self.hexToState[inputAddressList[0]]][self.hexToState[inputAddressList[1]]]);
            # if(t == int): self.state[self.hexToState[inputAddressList[0]]][self.hexToState[inputAddressList[1]]] = int(value);


    def printState(self):
        print("current frame number: ", self.state["frame"]);
        print("stage: ", self.state["stage"]);

        print("p1 x: ", self.state["p1"]["x"]);
        print("p1 y: ", self.state["p1"]["y"]);

        print("p2 x: ", self.state["p2"]["x"]);
        print("p2 y: ", self.state["p2"]["y"]);
