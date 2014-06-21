import socket
import threading
import SocketServer

"""
    TcpServer 或者UdpServer 均是阻塞式的服务，即请求是一个接着一个被处理的，如果有一个请求
    由于某种原因阻塞了，接下来的请求会放到请求队列里面，等待执行

    如果需要异步的处理请求，可以通过使用ThreadingMixIn来实现，实现类必须将ThreadingMixIn放在前面
    因为ThreadingMixIn重写了TCPServer中的某些方法

    异步方式处理请求可以减少阻塞，但由于是多线程异步处理，所以需要考虑必要的线程安全


    TCPServer ， UDPServer 均是从BaseServer处继承过来的，
    BaseServer中的一些接口说明如下：
    BaseServer.fileno()   返回server监听的socket的文件描述符（整形）,

    BaseServer.handle_request() 用于处理请求的接口方法， 该方法会依次调用 get_request() , verify_request() , process_request() 方法， 如果中途发生异常
        或者超时的情况，会调用对应的回调方法 handle_error() , handle_timeout()

    BaseServer.serve_forever(poll_interval=0.5)  一直监听服务端socket，直到服务被停止，poll_interval 表示检测服务是否被停止的间隔

    BaseServer.address_family   表示server 的socket所属的协议族，一般有 socket.AF_INET 和 socket.AF_UNIX 两种

    BaseServer.RequestHandlerClass 表示服务端用于处理请求的处理类，服务端针对每一个请求都会创建一个请求处理类的实例

    BaseServer.request_queue_size 服务端请求处理队列

    BaseServer.finish_request()  在这个方法里，才会正真的对每一个请求实例化一个请求处理类， 并调用该实例的handle方法


    BaseServer.handle_error(request,client_address)  当请求处理类发生异常时，会调用该方法对异常进行处理

    BaseServer.handle_timeout()


    BaseServer.process_request(request,client_address) 该方法会调用finish_request() 方法实例化一个
        请求处理类。因此如果需要的话， 可以在这个方法内部实现多线程处理请求，ForkingMixIn 和 ThreadingMixIn类就是做了类似的处理
        

    BaseServer.server_activate()  在服务端被初始化的时候，会调用该方法监听指定的socket，这个方法可以被子类覆盖

    BaseServer.verify_request(request,client_address) 该方法用于校验该请求是否运行被处理，通过返回True或者False，来实现用户请求的访问控制


RequestHandler 是用来处理client请求的实际处理接口， 他的实现类必须实现handle方法， 其中间包含了如下方法
    RequestHandler.finish()  主要是在处理完client请求后，做些收尾的工作，如资源回收，状态重置等工作，在handle方法之后调用，如果setup()方法抛了异常，该方法不会被调用

    RequestHandler.handle() 用于处理用户的请求，可以通过self.request , self.client_address, self.server 来获取请求对象、client地址socket，服务实例等对象

    RequestHandler.setup()  在handle之前调用，因此可以做一些资源、状态初始化的工作
    
        
    
"""

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = "{}: {}".format(cur_thread.name, data)
        self.request.sendall(response)


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

def client(ip,port, message):
    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    sock.connect((ip,port))
    try:
        sock.sendall(message)
        response = sock.recv(1024)
        print "Received: {}".format(response)
    finally:
        sock.close()


if __name__ == "__main__":
    #port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost" , 0

    server = ThreadedTCPServer((HOST,PORT),ThreadedTCPRequestHandler)

    ip,port = server.server_address

    #Start a thread with the server --- that thread will then start one more thread for each request

    server_thread = threading.Thread(target=server.serve_forever)

    #Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()

    print "Server loop running in thread:", server_thread.name

    client(ip,port,"hello world 1")
    client(ip,port,"hello world 2")
    client(ip,port,"hello world 3")
    client(ip,port,"hello world 4")

    server.shutdown()
    
