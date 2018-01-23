# this file will be moved into the plugin

import socket

command = None

HOST = 'localhost'    # The remote host
PORT = 8000              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        command = input()
        s.send(str.encode(command))
        if command == 'STOP':
            break

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
