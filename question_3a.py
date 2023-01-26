import socket
import random
import threading

quotes = ["I just wanna stay in that lavendar haze.(Lavendar Haze)",
"Roaring twenties, tossing pennies in the pool.(The 1)",
"So, make the friendship bracelets, take the moment and taste it.(You're On Your Own, Kid)",
"We're happy, free, confused and lonely in the best way.(22)",
"It must be exhausting always rooting for the anti-hero.(Anti-Hero)",
"I guess sometimes we all get. Some kind of haunted.(Midnight Rain)",
"Dear reader, if it feels like a trap. You're already in one.(Dear Reader)"]

def quote(clientSocket):
    random_quote = random.choice(quotes)
    clientSocket.sendall(random_quote.encode())
    clientSocket.close()
    
def main():

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.listen(5)
    
    while True:
          clientSock, addr = serverSocket.accept()
          print("Connection established from %s" % str (addr))
          thread = threading.Thread(target = quote, args = (clientSock, ))
          thread.start()

main()
