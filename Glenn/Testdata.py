import socketserver

class service(socketserver.BaseRequestHandler):
    def handle(self):
        data = 'dummy'
        print("Client connected with ", self.client_address)
        while len(data):
            data = self.request.recv(1024)
            self.request.send(data)

        print("Client exited")
        self.request.close()


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


t = ThreadedTCPServer(('', 12345), service)
t.serve_forever()