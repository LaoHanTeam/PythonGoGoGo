import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    RequestHandler ，用于处理请求
    """

    def handle(self):
        #self.request 一个和client建立连接的tcp Socket
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data

        #just send back the same data
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST , PORT = "localhost",9999

    #create the server
    server = SocketServer.TCPServer((HOST,PORT),MyTCPHandler)

    #keep running the server until you interrupt the program
    server.serve_forever()

