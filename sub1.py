import zmq

context=zmq.Context()
socket=context.socket(zmq.SUB)
socket.connect('tcp://127.0.0.1:5431')
socket.setsockopt(zmq.SUBSCRIBE,'')

while(True):
    message=socket.recv_pyobj()
    print(message)