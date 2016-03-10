
import socket as sc;
import os;


socketPath =  'socketTest'
socket = sc.socket(sc.AF_UNIX, sc.SOCK_DGRAM, 0);
### make sure the socket does not already exist
try: os.unlink(socketPath);
except OSError:
    if os.path.exists(socketPath): raise

## bind the socket to its path
socket.bind(socketPath);



while (True):
    print("waiting for socket input");
    datagram = socket.recv( 1024 ) # get the information from the socket
    print("datagram", datagram);
    n = input("enter something");
    print(n);




