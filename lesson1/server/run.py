# -*- coding: utf-8 -*-
import socket, os

def get_path(request):
    n = request.find("GET ")
    s = request[n+4:] 
    m = s.find(" ")   
    return s[0:m]


def get_response(request):
    copy = request
    n = copy.find("User-Agent")
    s = copy[n:]
    m = s.find("\n")
    path = get_path(request_string)
    if path == "/media/":
    	mes = ' '.join(os.listdir('files'))
    elif path == "/test/":
    	mes = request_string
    elif path == "/": 
	mes = "Hello mister!\nYou are: " + s[0:m]
    else:
	mes = "Page not found"
    return mes


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
        client_socket.close()
    except KeyboardInterrupt:  #
        print 'Stopped'
        server_socket.close()  #close connection
        exit()
