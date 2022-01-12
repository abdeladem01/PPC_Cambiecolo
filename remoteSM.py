from multiprocessing.managers import BaseManager as MyManager
from multiprocessing import Lock


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

    def acquire_mutex(self):
        self.mutex.acquire()

    def acquire_bell(self):
        self.bell.acquire

    def release_mutex(self):
        self.mutex.release()

    def release_bell(self):
        self.bell.release()


remote = MyRemoteClass()

MyManager.register('sm', callable=lambda: remote)
m = MyManager(address=("127.0.0.1", 8888), authkey=b'abracadabra')
s = m.get_server()
s.serve_forever()
