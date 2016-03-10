
import socket as sc;
import os;


socketPath = 'socketTest';
socket = sc.socket(sc.AF_UNIX, sc.SOCK_DGRAM, 0);

socket.connect("socketTest")

while(True):
    inputValue = input("> ");
    if(inputValue != ""):
        print("sending the data");
        socket.send(inputValue.encode('utf-8'))
        print("sent data");


