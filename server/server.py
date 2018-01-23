"""      *** SERVER ***

- SETPOS <int num> : set client's cursor position at <num>
- APPEND <int num> <str buffer> : append <buffer> to the <num> position in the text
? NAME <str buffer> : set client's firendly name to <name>
"""

import socket
import threading

# max number of bytes to be received from clients
RECV_BUF_SIZE = 1024

HOST = ''
PORT = 8000

# class Client?


# modified from : https://stackoverflow.com/questions/23828264/how-to-make-a-simple-multithreaded-socket-server-in-python-that-remembers-client

class ThreadedServer():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket
        self.sock.bind((self.host, self.port))  # bind it to given host & port
        self.clients = []  # list of clients

    def listen(self):
        self.sock.listen()
        while True:
            client, address = self.sock.accept()  # accept any new client
            client.settimeout(60)  # after this delay, clients must reconnect
            print('New connection:', address)
            threading.Thread(target=self.listenToClient,
                             args=(client, address)).start()
            self.clients.append(client)  # add client to list of clients

    def listenToClient(self, client, address):
        while True:
            try:
                data = client.recv(RECV_BUF_SIZE)  # receive data from clients
                if data:
                    str_data = data.decode()
                    if str_data.startswith('APPEND'):
                        print(str_data[7:])  # TODO: send the data to all clients
                    elif str_data.startswith('SETPOS'):
                        print('set position: ', str_data[7:])  # TODO: send the data to all clients
                    else:  # other commands go here...
                        print('unknown command')

                else:
                    raise ('Client {} disconnected'.format(address))
                    # need to remove client from the list
            except:
                client.close()
                # need to remove client from the list
                return False

    def sendToClients(self, message):
        for c in self.clients:
            try:
                c.send(message)
            except:
                print("error sending data to client. Maybe he disconnected?")
                # need to remove the client from the list


def main():
    ThreadedServer(HOST, PORT).listen()  # start the server


if __name__ == "__main__":
    main()
