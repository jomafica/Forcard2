from __future__ import annotations
from abc import ABC, abstractmethod
from requests import get
from retry import retry
import logging
from time import sleep

'''
ToDo

How to test
x = ConnectionStatus()
try:
    x.start('https://pplware.sapo.pt/')
except KeyboardInterrupt:
    ...

domain='https://pplware.sapo.pt/redes_sociais/twitter-estabelece-parceria-com-a-reuters-e-a-ap-para-detetar-desinformacao/'
connection = ConnectionStatus(StartConnection())
connection.start_connection(domain)

x = StartConnection()
domain='https://pplware.sapo.pt/redes_sociais/twitter-estabelece-parceria-com-a-reuters-e-a-ap-para-detetar-desinformacao/'
x.start(domain)

'''

'''
class ConnectionStatus:

    STATUS = False

    def __init__(self):
        self.domain = None
        self.http_code: Response

    def start(self, domain):
        if domain:
            self.domain = domain
            self._start_connection()
            if self.STATUS:
                self._health_check()

    def _get_status_code(self):
        try:
            self.http_code = get(self.domain, timeout=5)
        except:
            self.STATUS = False
            print('Lost Connection')
            self._retry_connection()

    def _start_connection(self):
        self._get_status_code()
        if self.http_code and self.http_code.status_code == 200 or self.http_code.status_code == 301:
            self.http_code.close()
            self.STATUS = True

    @retry(tries=10,
           delay=2, 
           backoff=2) 
    def _retry_connection(self):
        is_alive = get(self.domain, timeout=5)
        if is_alive.status_code:
            is_alive.close()
            self.STATUS = True
            self._health_check()
            
    def _health_check(self):
        while self.STATUS:
            print(f'Is he answering? {self.STATUS}')
            self._start_connection() 
            sleep(5)

    def interrupt(self) -> None:
        self.status = False
'''

class State(ABC):

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, stats: bool):
        self._status = stats

    @property
    def dom(self):
        return self._dom

    @dom.setter
    def dom(self, domain: str):
        self._dom = domain
    
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def get_status_code(self):
        pass

    @abstractmethod
    def start_connection(self):
        pass

    @abstractmethod
    def retry_connection(self):
        pass

    @abstractmethod
    def health_check(self):
        pass

class StartConnection(State):

    def start(self, domain):
        if domain:
            self._dom = domain
            self.start_connection()

    def get_status_code(self):
        try:
            self.http_code = get(self._dom, timeout=5)
        except:
            self._status = False
            print('Lost Connection')
            self.retry_connection()

    def start_connection(self):
        self.get_status_code()
        if self.http_code and self.http_code.status_code == 200 or self.http_code.status_code == 301:
            self.http_code.close()
            self._status = True

    @retry(tries=10,
           delay=2, 
           backoff=2) 
    def retry_connection(self):
        is_alive = get(self._dom, timeout=5)
        if is_alive.status_code:
            is_alive.close()
            self._status = True
            self.health_check()

    def health_check(self):
        self.start_connection() 

