# -*- coding: utf-8 -*-
import socket, sys


def get_response(request):
    copy = request
    n1 = copy.find("User-Agent")
    s1 = copy[n1:]
    m1 = s1.find("\n")
    return "Hello mister!\nYou are: " + s1[0:m1] + request_string

def get_path(request):
    n = request.find("GET ")
    s = request[n+4:] 
    m = s.find(" ")  
    path = s[0:m] 
    return s[0:m]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  #connect to localhost to 8000 port
server_socket.listen(1)  #start listen, with max number clients of connection

print 'Started'

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print 'Got new client', client_socket.getsockname()  #to printing client`s ip and port 
        request_string = client_socket.recv(2048)  #reading 2048 bytes from socket  
        client_socket.send(get_response(request_string))  #messege to client some request
	client_socket.send(get_path(request_string))
	
        client_socket.close()
    except KeyboardInterrupt:  #
        print 'Stopped'
        server_socket.close()  #close connection
        exit()
