
import pyautogui
from time import sleep
screenWidth, screenHeight = pyautogui.size() 
currentMouseX, currentMouseY = pyautogui.position()
def sleep_time(times: int) -> sleep: return int(times)
seconds = sleep_time(int(input('Time to sleep(s): ')))
print('To break loop press CTRL + C')
try:
    while True:
        pyautogui.click()
        print(f'Just clicked! Now i will sleep {seconds} seconds')
        sleep(seconds) 
except KeyboardInterrupt:
    pass


'''

"""State class: Base State class"""
class State:
  
    """Base state. This is to share functionality"""
  
    def scan(self):
          
        """Scan the dial to the next station"""
        self.pos += 1
  
        """check for the last station"""
        if self.pos == len(self.stations):
            self.pos = 0
        print("Visiting... Station is {} {}".format(self.stations[self.pos], self.name))
  
"""Separate Class for AM state of the radio"""
class AmState(State):
  
    """constructor for AM state class"""
    def __init__(self, radio):
          
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"
  
    """method for toggling the state"""
    def toggle_amfm(self):
        print("Switching to FM")
        self.radio.state = self.radio.fmstate
  
"""Separate class for FM state"""
class FmState(State):
  
    """Constriuctor for FM state"""
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"
  
    """method for toggling the state"""
    def toggle_amfm(self):
        print("Switching to AM")
        self.radio.state = self.radio.amstate
  
"""Dedicated class Radio"""
class Radio:
  
    """A radio. It has a scan button, and an AM / FM toggle switch."""
  
    def __init__(self):
          
        """We have an AM state and an FM state"""
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate
  
    """method to toggle the switch"""
    def toggle_amfm(self):
        self.state.toggle_amfm()
  
    """method to scan """
    def scan(self):
        self.state.scan()
  
""" main method """
if __name__ == "__main__":
  
    """ create radio object"""
    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
    actions *= 2
  
    for action in actions:
        action()


'''






 
    
# Test (apagar)
#oldSet = {'786420', '786353', '786347', '786301', '786335'}
#currentSet = {'786425', '786424', '786422', '786421', '786420', '786353', '786347', '786301', '786335'}
#z = currentSet.difference(oldSet)
#print(z)
################################################
#yz = BeautifulSoup(fetch_body, 'html.parser')
#y = [yz.find_all("article")[0]]
#print(y)
################################################
# Test (apagar)
#yz = BeautifulSoup(fetch_body, 'html.parser')
#y = set()
#for e in yz.find_all("article"):
#    rx = re.search(r'[^post-]+.', e['id'])
#    y.add((rx.group(0),e.a['href']))
#for ih in y:
#    (id, href) = ih
#    print(id)


#if __name__ == "__main__":
#    main()



'''
Get post ID, not finished!
Result: set{'786420', '786353', '786347', '786301', '786335'}
'''
#with open('resul.html', 'w', encoding="utf-8") as f:
#    x = []
#    y = set()
#    for e in html_body.find_all("article"):
#        x.append(e)
#        y.add(e.a['href'])
#    print(y)
#    f.write(str(x))
#f.close()
##y = set()
##for e in html_body.find_all("article"):
##  rx = re.search(r'[^post-]+.', e['id'])
##  y.add(rx.group(0))      
## print(y)






'''
Requirements:
C    <h1 class="post-title">Lakka: A distro que transforma o seu PC numa consola retro</h1> 
C    <time datetime="2021-08-02T23:00:40+01:00">02 Ago 2021</time>
C    <a href="https://pplware.sapo.pt/category/linux/" title="Ver todos os artigos de Linux">Linux</a><span class="comments-link"><a href="https://pplware.sapo.pt/linux/lakka-a-distro-que-transforma-o-seu-pc-numa-consola-retro/#comments">1 Comentário</a></span>   
    <p>Pela internet existem projetos fantásticos... e gratuitos. O que damos a conhecer hoje chama-se Lakka, e é uma distribuição Linux que transforma facilmente o&nbsp;seu PC numa consola retrogaming.</p>
    <p>Conheça melhor esta distribuição que é baseada na LibreELEC.</p>
C   <p><a target="_blank" href="https://pplware.sapo.pt/wp-content/uploads/2021/08/lakka-retrogaming-linux.jpe"><img loading="lazy" src="https://pplware.sapo.pt/wp-content/uploads/2021/08/lakka-retrogaming-linux-720x405.jpe" alt="" width="720" height="405" class="aligncenter size-medium wp-image-787617" srcset="https://pplware.sapo.pt/wp-content/uploads/2021/08/lakka-retrogaming-linux-720x405.jpe 720w, https://pplware.sapo.pt/wp-content/uploads/2021/08/lakka-retrogaming-linux-150x84.jpe 150w, https://pplware.sapo.pt/wp-content/uploads/2021/08/lakka-retrogaming-linux-768x432.jpe 768w, https://pplware.sapo.pt/wp-content/uploads/2021/08/lakka-retrogaming-linux-345x194.jpe 345w, https://pplware.sapo.pt/wp-content/uploads/2021/08/lakka-retrogaming-linux-50x28.jpe 50w, https://pplware.sapo.pt/wp-content/uploads/2021/08/lakka-retrogaming-linux.jpe 800w" sizes="(max-width: 720px) 100vw, 720px"></a></p>
    <h3>Distribuição Linux Lakka tem suporte para Raspberry Pi</h3>
    <p>A distribuição Linux Lakka é um sistema "amigável" uma vez que é fácil de configurar e usar. Além disso, esta distribuição é também, “poderosa” graças ao facto de usar o RetroArch, o conhecido frontend multiplataforma para emuladores, videojogos, etc.</p>
    <p>Esta distribuição suporta vários tipos de hardware como o Raspberry Pi e outros mini-PCs semelhantes. A distribuição Linux Lakka é um projeto Open Source desenvolvido pela comunidade sendo baseado na popular distribuição Linux LibreELEC, uma distribuição destinada a sistemas multimédia.</p>
    <p>A distro Lakka é capaz de transformar um computador numa consola de jogos retro, com recurso a emuladores. Além da imagem x86 tradicional,&nbsp; suporta Raspberry Pi 0/W, Raspberry Pi, Raspberry Pi 2, Raspberry Pi 3, Raspberry Pi 4, I.MX6 Cubox-I, I.MX6 UDOO, I.MX6 Wandboard, Odroid XU3 /4, Allwinner, Amlogic, Rockchip, Odroid Go Advance, Ambernic RG351P / M, Ambernic RG351V e Nintendo Switch.</p>
    <p>Ao nível das consolas ou plataformas de videojogos, é capaz de emular a antiga Nintendo NES, Super Nintendo, Mega Drive (Sega Genesis no mercado norte-americano), PlayStation, jogos Arcade e muito mais graças ao RetroArch.</p>
    <p>Num próximo artigo iremos ensinar como podem usar esta distribuição. Estejam atentos.</p>
C   <h3><a href="https://pplware.sapo.pt/author/ppinto/" title="Artigos de Pedro Pinto" rel="author">Pedro Pinto</a></h3>




    JSONBODY:
    {
    "id": "POST_ID"
    "article": "ARTICLE_URL"
    "time": "DATE_TIME"
    "comments": "COMMENTS"
    "type":"CONTENT_TYPE"
    "author":"AUTHOR"
    "title": "ARTICLE_TITLE"
    "image": "URL_IMAGE"   
    "content":"ARTICLE_DOC"
    }
'''


'''
class ConnectionRetry(ConnectionStatus):

    @retry(tries=3, delay=2, backoff=15)
    def check_statusCode(self, url):
        try:
            self.body_content = get(url, timeout=5)
            if self.body_content:
                _status = self.body_content.status_code
                if _status == 200 or _status == 301:
                    return True
        except:
            return self.check_existence(url)

    def content_body(self):
        return self.body_content.content

    def check_existence(self, domain):
        try:
            _host_up = self.check_connectivity(domain)
            if _host_up:
                return True
        except:
            print("Domain does not exist")

    def check_connectivity(self, domain):
        _strip_domain = search(r'[\w+\.]*\w+\.\w+', str(domain)) 
        try:
            _h_name = gethostbyname(_strip_domain.group(0))
            if _h_name:
                _reachable = self.check_reachability(_h_name,443)
                if _reachable:  
                    return True
        except:
            print('Could not translate the domain')

    def check_reachability(self, ip, port):
        try:
            _alive = self.retry_connection(ip, port)
            if _alive:
                return True
        except:
            print("Ip is not alive")

    @retry(tries=3, delay=2, backoff=15)   
    def retry_connection(self, ip, port):
        with create_connection((ip,port)) as _connected:
            if _connected:
                _connected.close()
                return True
                
    


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
class ConnectionStatus:

    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current state of the Context.
    """

    _state = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        The Context allows changing the State object at runtime.
        """
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    The Context delegates part of its behavior to the current State object.
    """

    def start_connection(self, domain: str):
        self._state.start_session(domain)

    def current_state(self):
        self._state.current_session()

    def recover_connection(self):
        self._state.retry_connection()

class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    @property
    def context(self) -> ConnectionStatus:
        return self._context

    @context.setter
    def context(self, context: ConnectionStatus) -> None:
        self._context = context

    @property
    def status(self) -> ConnectionStatus:
        return self._context
    
    @status.setter
    def status(self, sts) -> None:
        self._context = context

    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def get_status_code(self) -> None:
        pass

    @abstractmethod
    def start_connection(self) -> None:
        pass

    @abstractmethod
    def retry_connection(self) -> None:
        pass

    @abstractmethod
    def health_check(self) -> None:
        pass


"""
Concrete States implement various behaviors, associated with a state of the
Context.
"""   

class StartConnection(State):

    def start_session(self, domain: str) -> None:
        if domain:
            self.domain = domain
            if self._start_connection():
                self.context.transition_to(CurrentStatus())
            self.context.transition_to(RetryConnection())

    def _start_connection(self):
        self._get_status_code()
        if self.http_code and self.http_code.status_code == 200 or self.http_code.status_code == 301:
            self.http_code.close()
            return True

    def _get_status_code(self):
        try:
            self.http_code = get(self.domain, timeout=5)
        except:
            print('Lost Connection')
            self.context.transition_to(RetryConnection())

class CurrentStatus(State):
    def current_session(self):
        if self._start_connection():
            print('True')
        self.context.transition_to(RetryConnection())

    def _start_connection(self):
        self._get_status_code()
        if self.http_code and self.http_code.status_code == 200 or self.http_code.status_code == 301:
            self.http_code.close()
            return True

    def _get_status_code(self):
        try:
            self.http_code = get(self.domain, timeout=5)
        except:
            print('Lost Connection')
            self.context.transition_to(RetryConnection())

class RetryConnection(State):

    @retry(tries=10,
           delay=2, 
           backoff=2) 
    def retry_connection(self):
        is_alive = get(self.domain, timeout=5)
        if is_alive.status_code:
            is_alive.close()
            self.context.transition_to(StartConnection())








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
            if self._status:
                self.health_check()

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
        while self._status:
            print(f'Is he answering? {self._status}')
            self.start_connection() 
            sleep(5)



'''