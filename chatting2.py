import threading
import socket
def write1():
    while True:
        text=input("Enter : ")
        tex.sendall(text.encode('utf-8'))

def lis():

    while True:
     print("from client : ",tex.recv(5005).decode())

if __name__=="__main__":
    s=socket.socket()
    s.bind(('',5005))
    s.listen(1)
    print("socket is listening")
    t='hiii'
    tex, con = s.accept()

    t1=threading.Thread(target=write1,name='t1')
    t2=threading.Thread(target=lis,name='t2')
    t1.start()
    t2.start()