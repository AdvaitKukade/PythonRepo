import socket
import threading

def write():
    while True:
        text = input("Enter : ")
        s.send(bytes(text,'utf-8'))
        #tex.sendall(text.encode('utf-8'))


def lis():
    while True:
        print("from server : ",s.recv(5005).decode())

#print(s.recv(5005))
#print("data printed")
#s.close()
if __name__=="__main__":
 t='192.168.225.82'
 p=5005
 s=socket.socket()
#s.connect(t,p)
 s.connect(('192.168.225.1',p))

 t1=threading.Thread(target=write,name='t1')
 t2=threading.Thread(target=lis,name='t2')
 t1.start()
 t2.start()