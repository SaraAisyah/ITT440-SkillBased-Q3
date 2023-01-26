import socket

def main():
  
  clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  clientSocket.connect(("192.168.234.128",8888))
  
  data = clientSocket.recv(1024)
  print("Random quotes from a song: %s" % data.decode())
  
  clientSocket.close()
  
main()
