import socket

		
s=socket.socket()
s.bind(('127.0.0.1',9999))
(conn,addr)=s.accept()
s.listen(2)
	
while True:
		filename='C:/hosts'
		s.send(filename.encode('utf-8'))
		str1 = s.recv(1024)
		str2=str1.decode('utf-8')
		if str2=='no':
			print('Your please is failed!' % filename)
		else:
			s.send(b'I am ready!')
		temp=filename.split('/')
		myname='my_'+temp[len(temp)-1]
		size=1024
		with open(myname,'wb') as f:
			while True:
				data=s.send(size)
				f.write(data)
				if len(data)<size:
					break
		print('The recv file is %s.' % myname)

		s.close()
	