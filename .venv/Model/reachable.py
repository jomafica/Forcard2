from requests import get, Response
from retry import retry
import logging
from time import sleep

'''
ToDo
 -

How to test
x = ConnectionStatus()
try:
    x.start('https://pplware.sapo.pt/')
except KeyboardInterrupt:
    ...
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
            #print(f'Is he answering? {self.STATUS}')
            self._start_connection()
            sleep(5)

    def interrupt(self) -> None:
        self.status = False



