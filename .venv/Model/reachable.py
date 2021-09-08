from __future__ import annotations
from abc import ABC, abstractmethod
from requests import get
from enum import Enum, auto
from retry import retry
# import logging # to be implemented

class Status(Enum):
    """ Connection status """

    IDLE = auto()
    OK = auto()
    RECONNECTING = auto()
    LOSTCONNECTION = auto()

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
        self.status = Status.IDLE
        self.domain: str =  None
        self.http_code: str = None
        self.info: str = None

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
            self.context.status = Status.LOSTCONNECTION
        self.context.http_code = get(self.context.domain, timeout=5)


    def start_connection1(self):
        self.get_status_code1()
        if self.context.http_code and self.context.http_code.status_code in [
            200,
            301,
        ]:
            self.context.http_code.close()
            self.context.status = Status.OK
            self.context.transition_to(HealthCheck()) # Make this better
             

    def retry_connection1(self): ...
    def health_check1(self): ...

class HealthCheck(State):

    def health_check1(self):
        self.start_connection1()
            

    def start_connection1(self):
        self.get_status_code1()
        if self.context.http_code and self.context.http_code.status_code in [
            200,
            301,
        ]:
            self.context.http_code.close()
            # logging here


    def get_status_code1(self):
        try:
            self.context.http_code = get(self.context.domain, timeout=5)
        except:
            self.context.http_code = None
            self.context.status = Status.LOSTCONNECTION
            #print('Lost Connection') 
            self.context.transition_to(RetryReconnection())
               

    def start1(self): ...
    def retry_connection1(self): ...

class RetryReconnection(State):

    @retry(tries=10,
           delay=2, 
           backoff=2) 
    def retry_connection1(self):
        self.context.status = Status.RECONNECTING
        self.context.http_code = get(self.context.domain, timeout=5)
        if self.context.http_code.status_code:
            self.context.http_code.close()
            self.context.status = Status.OK
            self.context.transition_to(HealthCheck())

    def start1(self): ...

    def health_check1(self): ...






""" 
for teste porpuses 
"""
#import asyncio 
#async def health_check2(taskss):
#    while taskss.status == Status.OK:
#        taskss.health_check()
#        await asyncio.sleep(2)
#    if taskss.status == Status.LOSTCONNECTION:
#        taskss.retry_connection()
#    if taskss.status == Status.OK:
#        asyncio.create_task(health_check2(taskss))
#
#async def program(prog):
#    while Status.OK:
#        if prog.status != Status.OK:
#            await asyncio.sleep(10)
#        await asyncio.sleep(2)
#
#async def main(objt):
#    await asyncio.gather(health_check2(objt), program(objt))
#    
#    
#domain='https://pplware.sapo.pt/'
#x = ConnectionStatus(StartConnection())
#x.start(domain)
#asyncio.run(main(x))
#print('finish')