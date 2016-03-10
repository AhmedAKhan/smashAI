import os;
import socket as sc;
import debugger as dgr;
import binascii;
import time;

"""
    This is how dolphines memory watcher uses the data
    MemoryWatcher reads a file containing in-game memory addresses and outputs
    changes to those memory addresses to a unix domain socket as the game runs.

    The input file is a newline-separated list of hex memory addresses, without
    the "0x". To follow pointers, separate addresses with a space. For example,
    "ABCD EF" will watch the address at (*0xABCD) + 0xEF.
    The output to the socket is two lines. The first is the address from the
    input file, and the second is the new value in hex.
"""

class MemoryWatcher:
    """
        create a socket
        unix domain socket
        flags = 0
        socket type = SOCK_DGRAM, other options include SOCK_STREAM, SOCK_RAW, SOCK_RDM, SOCK_SEQPACKET
        SOCK_DGRAM = faster, data might not always reach its destination.
        SOCK_STREAM = garuntees order, and relative garuntee that message was successfully sent,
    """
    def __init__(self, path):
        self.socket = sc.socket(sc.AF_UNIX, sc.SOCK_DGRAM, 0);
        self.path = path; # the path to where dolphin emulator is stored
        self.createEmptyState();
    def createEmptyState(self):
        self.state = {
            "playerOne":{
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
                "menuState":0,
                "Stage":0,
                "x":0,
                "y":0
            },
            "playerTwo":{
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
                "menuState":0,
                "Stage":0,
                "x":0,
                "y":0,

                "cursorX":0,
                "cursorY":0
            },
            "Frame":0,
        };

    def startSocket(self):
        socketPath =  self.path + "/MemoryWatcher" + '/MemoryWatcher' # this is the path to the socket
        ### make sure the socket does not already exist
        try: os.unlink(socketPath);
        except OSError:
            if os.path.exists(socketPath): raise

        ## bind the socket to its path
        self.socket.bind(socketPath);
        # dgr.dprint("binded the socket waiting for input");
    def test(self):
        while True:
            dgr.dprint("starting to read from socket");
            datagram = self.socket.recv( 1024 ) # get the information from the socket
            if not datagram: break # break out if the information is null

            dgr.dprint("-" * 20) ## print a line just to make it easier to read
            dgr.dprint(datagram) ## print the information

        self.socket.close();
        return;

    """
        this function will delay for the number of frames that is given by the user
        @param 1 = delay, the amount that you want to delay it.
    """
    def pauseForTime(self, delay):
        if(not self.socket):
            print("the socket has not been created yet please create it before calling the pauseForTime function");
            return;
        # print("inside the pause for delay");
        numberOfFramesPassed = 0;
        startingFrame = -1;
        # print("still paused");
        while(True):
            datagram = self.socket.recv( 1024 ) # get the information from the socket
            # print (datagram)
            datagram = datagram.splitlines();
            region = datagram[0].decode('ascii');
            value = int(datagram[1][0:-1],16); ## remove the last null character
            if(region != "00479D60"): continue;

            numberOfFramesPassed += 1;
            if(startingFrame == -1):
                startingFrame = value;

            print("number of frames passed: " + str(numberOfFramesPassed), "delay: ", delay, "value: ", value, "startingFrame: ", startingFrame)
            # if(value >= startingFrame + delay):
            #     print("exiting because of condition 1");
            #     return;

            if(numberOfFramesPassed >= delay):
                print("exiting because of condition 2");
                return;


    def getX(self):
            datagram = self.socket.recv( 1024 )
            datagram = datagram.splitlines();
            region = datagram[0].decode('ascii');

            if "00453F20" in region:
                x=((int(datagram[1].decode('ascii')[:-1],16)))
                print(x)
                return(x)
            else:
                return 0


    def getHitStun(self):
            datagram = self.socket.recv( 1024 )
            datagram = datagram.splitlines();
            region = datagram[0].decode('ascii');

            if region == "00453FC0 23a0":
                x=((int(datagram[1].decode('ascii')[:-1],16)))
                # x=((int(datagram[1].decode('ascii'),16)))
                # print("hexcode value: " + str(datagram[1]));
                print("hitStun value: " + str(x))
                # return(x)
                return;
            else:
                return -1

    def adjustValue(self, region, value):
        # print("region: ", region, "value:",value);
        if(region == "00479D60"):
            print("value: ",value, "currentFrame: ", int(value[0:-1],16));

        # if(region.find(" ") != -1):
        #     baseInt = "";
        #     if(baseInt == "0x453130"):
        #         print("");
        #     elif(baseInt == "asdasd"):
        #         print("");
        # else:
        #     print("");

    def readMemory(self):
        if(not self.socket):
            print("the socket has not been created yet please create it before calling the pauseForTime function");
            return;
        datagram = self.socket.recv( 1024 ) # get the information from the socket
        # print (datagram)
        datagram = datagram.splitlines();
        region = datagram[0].decode('ascii');
        value = datagram[1];
        self.adjustValue(region, value);








# if __name__ == '__main__':
#     main();


