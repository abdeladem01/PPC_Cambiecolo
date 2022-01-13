from multiprocessing.managers import BaseManager as MyManager
from multiprocessing import Lock
#Defining Remote Managed Class...
class MyRemoteClass:
    def __init__(self, number):
        self.available = {}
        self.offer = {}
        self.mutex = Lock()
        self.bell=Lock()
    def get_flag(self):
        return self.available
    def set_flag(self, pushed_bool, key):
        self.available[key] = pushed_bool
    def get_offers(self):
        return self.offers
    def set_offers(self, pushed_list, key):
        self.offers[key] = pushed_list
    def acquire_mutex(self): #Shared mutex on SM
        self.mutex.acquire()
    def release_mutex(self):
        self.mutex.release()
    def acquire_bell(self): #Shared mutex on bell
        self.bell.acquire
    def release_bell(self):
        self.bell.release()

remote = MyRemoteClass() #Creating an object remote from this class
MyManager.register('sm', callable=lambda: remote)  #registring the remote on shared memory with the manager class 
m = MyManager(address=("127.0.0.1", 8888), authkey=b'abracadabra') #from the documentation, needs changes
s = m.get_server() #return the actual server under the control of the Manager
s.serve_forever() #start and run it forever