import threading
import socket			
import time
import random
import sys

class counter():					
	port = 0
	
class Client:						
	def cli(self):					
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:	
			server_socket.bind((socket.gethostname(), int(counter.port)))
			server_socket.listen(1)
			server_socket.settimeout(1)
			len = random.randint(1,128)
			count = 0
			string = ""
			while count < len:
				temp = random.randint(33,126)
				string = string + unichr(temp)
				count = count + 1
			while 1:
				newConnection, client = server_socket.accept()
				newConnection.send(str(string))
				newConnection.close()
				return
		except socket.error:										
			return
        
class ThreadClass(threading.Thread):
	def run(self):
		client = Client()						
		client.cli()	
		return
        
if __name__ == "__main__":	
	print "Fakeport Machine 0.1"	
	print "CTRL-C to exit"
	try:
		if not(str(sys.argv[1]).isdigit()):
			print "Usage fakeport.py range" 
			print "Example: python fakeport.py 1 1024"
			print "ERROR: Invalid Lower Port Number"									
			sys.exit()															
		port1 = int(sys.argv[1])
		if port1 > 65535:
			print "Usage fakeport.py range" 
			print "Example: python fakeport.py 1 1024"
			print "ERROR: Port Number To High 0-65545"								
			sys.exit()
	except IndexError:
		print "Usage fakeport.py range" 
		print "Example: python fakeport.py 1 1024"
		sys.exit()
	try:
		if not(str(sys.argv[2]).isdigit()):
			print "Usage fakeport.py range" 
			print "Example: python fakeport.py 1 1024"
			print "ERROR: Invalid Higher Port Number"									
			sys.exit()															
		port2 = int(sys.argv[2])
		if port2 > 65535:
			print "Usage fakeport.py range" 
			print "Example: python fakeport.py 1 1024"
			print "ERROR: Port Number To High 0-65545"								
			sys.exit()		
		if port1 > port2:
			print "Usage fakeport.py range" 
			print "Example: python fakeport.py 1 1024"
			print "ERROR: Invalid Port Range - Lower value can not greater than higher"								
			sys.exit()
	except IndexError:
		print "Usage fakeport.py range" 
		print "Example: python fakeport.py 1 1024"
		sys.exit()
	try:
		while True:
			counter.port = random.randint(port1,port2)	
			t = ThreadClass()
			t.start()
			time.sleep(0.01)
	except KeyboardInterrupt:	
		print "Goodbye"
