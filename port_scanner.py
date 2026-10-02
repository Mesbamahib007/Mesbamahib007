import socket
target_ip ="127.0.0.1"
port = 80
s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
result = s.connect_ex((target_ip,port))
if result == 0:
	print(f"Port {port} is open!")
else:
	print(f"Port {port} is CLOSED or filtered.")
s.close()
