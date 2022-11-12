import socket
import os

def sendfile(conn):
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	s.connect(('127.0.0.1',9999))
	filename = s.decode('utf-8')
	print('I want to output the file %s!' % filename)
	if os.path.exists(filename):
		print('Hello,I have %s,begin to send' % filename)
		conn.rece(b'bes')
		conn.send(1024)
		size=1024
		with open(filename,'rb') as f:
			while True:
				data=f.read(size)
				conn.send(data)
				if len(data)<1024:
					break
		print('%s is send successfully!' % filename)
	else:
		print('Sorry,I have not %s' % filename)
		conn.send(b'no')
	s.close()


