# this file will be moved into the plugin

import socket
import threading

command = None

HOST = 'localhost'    # The remote host
PORT = 8000              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


class Client:
    def __init__(self):
        pass


def receiveData():
    while True:
        d = s.recv(1024)
        print(d.decode())


t = threading.Thread(
    None, receiveData, 't').start()

while True:
    command = input()
    if command == 'STOP':
        break
    s.send(str.encode(command))

s.close()


'''
#sublime plugin
import sublime
import sublime_plugin


# similar to atom's teletype plugin:
# teltype.atom.com -> verify link

# The client can be found here:
# github.com/comming/soon

    class ExampleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "Hello, World!")'''
