import socket

udp_ip = "0.0.0.0"
udp_port = 4210

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udp_ip, udp_port))

print("Listening for UDP packets...")
while True:
    data, addr = sock.recvfrom(1024)
    print("Received:", data.decode())
