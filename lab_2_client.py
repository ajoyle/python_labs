#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 2 - udp_local.py
# UDP client and server on localhost

import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

MAX = 65535
PORT = 22


print 'Address before sending:', s.getsockname()
#s.sendto('This is my message', ('127.0.0.1', PORT))
s.sendto('Anderson Joyle texto', ('locahost', PORT))
print 'Address after sending', s.getsockname()
data, address = s.recvfrom(MAX) # overly promiscuous - see text!
print 'The server', address, 'says', repr(data)
