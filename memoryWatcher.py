#import socket module
import os;
import socket as sc;

#### from the dolphin documentation
## MemoryWatcher reads a file containing in-game memory addresses and outputs
## changes to those memory addresses to a unix domain socket as the game runs.
##
## The input file is a newline-separated list of hex memory addresses, without
## the "0x". To follow pointers, separate addresses with a space. For example,
## "ABCD EF" will watch the address at (*0xABCD) + 0xEF.
## The output to the socket is two lines. The first is the address from the
## input file, and the second is the new value in hex.
##
##

class MemoryWatcher:

    def __init__(self, path):
        # create a socket
            # unix domain socket
            # flags = 0
            # socket type = SOCK_DGRAM, other options include SOCK_STREAM, SOCK_RAW, SOCK_RDM, SOCK_SEQPACKET
            # SOCK_DGRAM = faster, data might not always reach its destination.
            # SOCK_STREAM = garuntees order, and relative garuntee that message was successfully sent,
        self.socket = sc.socket(sc.AF_UNIX, sc.SOCK_DGRAM, 0);
        self.path = path; # the path to where dolphin emulator is stored
    def startSocket(self):
        ### make sure the socket does not already exist
        socketPath =  self.path + "/MemoryWatcher" + '/MemoryWatcher' # this is the path to the socket
        try: os.unlink(socketPath);
        except OSError:
            if os.path.exists(socketPath): raise

        ## bind the socket to its path
        self.socket.bind(socketPath);
        print("binded the socket waiting for input");

    def test(self):
        while True:
            print("starting to read from socket");
            datagram = self.socket.recv( 1024 ) # get the information from the socket
            if not datagram: break # break out if the information is null

            print("-" * 20) ## print a line just to make it easier to read
            print(datagram) ## print the information

        self.socket.close();

    """
      this function will call the function that has been inputed by the user
      @param 1 = fun = the function that you want to input
      @param rest = *args = the rest of the arguments you want the function to be called with
    """
    def runAfterFrames(delay, fun, *args):
        return fun(*args);

# if __name__ == '__main__':
#     main();




