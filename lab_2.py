import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

MAX = 65535
PORT = 22

s.bind(('localhost', PORT))
print 'Listening at', s.getsockname()

while True:
	data, address = s.recvfrom(MAX)
	print 'The client at', address, 'says', repr(data)
	s.sendto('Your data was %d bytes' % len(data), address)
