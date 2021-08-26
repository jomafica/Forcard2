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


'''
Criar state pattern here 

https://refactoring.guru/design-patterns/state/python/example

'''


class ConnectionStatus():

    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """
    _state = None

    """
    A reference to the current state of the Context.
    """

    def __init__(self, state: State) -> None:
        self.transition_to(state)
        self.domain: str =  None
        self.http_code: str = None
        self.status: bool = False

    def transition_to(self, state: State):
        """
        The Context allows changing the State object at runtime.
        """

        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def __str__(self):
        return type(self._state).__name__

    """
    The Context delegates part of its behavior to the current State object.
    """

    def start(self, domain):
        self._state.start1(domain)

    def get_status_code(self):
        self._state.get_status_code1()

    def get_status_code(self):
        self._state.get_status_code1()

    def start_connection(self):
        self._state.start_connection1()

    def retry_connection(self):
        self._state.retry_connection1()
    
    def health_check(self):
        self._state.health_check1()

class State(ABC):

    @property
    def context(self) -> ConnectionStatus:
        return self._context

    @context.setter
    def context(self, context: ConnectionStatus) -> None:
        self._context = context

    @abstractmethod
    def start1(self) -> None:
        pass

    @abstractmethod
    def get_status_code1(self) -> None:
        pass

    @abstractmethod
    def start_connection1(self) -> None:
        pass

    @abstractmethod
    def retry_connection1(self) -> None:
        pass

    @abstractmethod
    def health_check1(self) -> None:
        pass

class StartConnection(State):

    def start1(self, domain):
        if domain:
            self.context.domain = domain
            self.start_connection1()

    def get_status_code1(self):
        try:
            self.context.http_code = get(self.context.domain, timeout=5)
        except:
            self.context.status = False
            print('Not reachable')

    def start_connection1(self):
        self.get_status_code1()
        if self.context.http_code and self.context.http_code.status_code == 200 or self.context.http_code.status_code == 301:
            self.context.http_code.close()
            self.context.status = True
            print(f'Inside start connection status: {self.context.status}')
            self.context.transition_to(CurrentState())
             
    def retry_connection1(self): ...

    def health_check1(self): ...

class CurrentState(State):

    def health_check1(self):
        print('Inside Health Check def()')
        print(f'Inside health check status: {self.context.status}')
        self.start_connection1() 
    
    def start_connection1(self):
        self.get_status_code1()
        if self.context.http_code and self.context.http_code.status_code in [
            200,
            301,
        ]:
            self.context.http_code.close()
            self.context.status = True
            print('terminei segmento')
            return
        self.context.transition_to(RetryReconnect())

    def get_status_code1(self):
        try:
            self.context.http_code = get(self.context.domain, timeout=5)
        except:
            self.context.http_code = None
            self.context.status = False
            print('Lost Connection')   

    def start1(self): ...

    def retry_connection1(self): ...

class RetryReconnect(State):

    @retry(tries=10,
           delay=2, 
           backoff=2) 
    def retry_connection1(self):
        print('trying')
        print(self.context.domain)
        self.context.http_code = get(self.context.domain, timeout=5)
        if self.context.http_code.status_code:
            self.context.http_code.close()
            self.context.status = True
            self.context.transition_to(CurrentState())

    def start1(self): ...

    def get_status_code1(self): ...

    def start_connection1(self): ...

    def health_check1(self): ...


domain='https://pplware.sapo.pt/'
x = ConnectionStatus(StartConnection())
x.start(domain)
current_status = [x]
while x.status:
    print('Inside while loop:',x.status)
    if x in current_status:
        x.health_check()
        print(x)
    sleep(3)
x.retry_connection()


print('Outside while loop:',x.status)
print('finish')