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
    def startSocket(self):
        socketPath =  self.path + "/MemoryWatcher" + '/MemoryWatcher' # this is the path to the socket
        ### make sure the socket does not already exist
        try: os.unlink(socketPath);
        except OSError:
            if os.path.exists(socketPath): raise

        ## bind the socket to its path
        self.socket.bind(socketPath);
        dgr.dprint("binded the socket waiting for input");
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
        print("inside the pause for delay");
        numberOfFramesPassed = 0;
        while(True):
            datagram = self.socket.recv( 1024 ) # get the information from the socket
            print (datagram)
            datagram = datagram.splitlines();
            region = datagram[0].decode('ascii');
            if(region == "00479D60"):
                numberOfFramesPassed += 1;
                print(numberOfFramesPassed)
            if(numberOfFramesPassed >= delay):
                return;



# if __name__ == '__main__':
#     main();




