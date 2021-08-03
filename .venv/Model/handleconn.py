import requests
import re
import socket
from retry import retry

''' ToDo here: 
  - System process
  - HealthCheck 
'''
class HandleConnection:

    def __init__(self, link_url, bodyContent=None):
        self.url = link_url
        self.bodyContent = bodyContent

    def start(self):
        # initiate process(create a new class for system process and call it here)
        if self.check_statusCode(self.url):
            return self.content_body()
        else:
            return False

    @retry(tries=3, delay=2, backoff=15)
    def check_statusCode(self, url):
        try:
            self.bodyContent = requests.get(url, timeout=1)
            if self.bodyContent:
                _status = self.bodyContent.status_code
                if _status == 200:
                    return True
        except:
            return self.check_existence(url)

    def content_body(self):
        return self.bodyContent.content

    def check_existence(self, domain):
        try:
            _host_up = self.check_connectivity(domain)
            if _host_up:
                return True
        except:
            print("Domain does not exist")

    def check_connectivity(self, domain):
        _strip_domain = re.search(r'[\w+\.]*\w+\.\w+', str(domain)) 
        try:
            _h_name = socket.gethostbyname(_strip_domain.group(0))
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
        with socket.create_connection((ip,port)) as _connected:
            if _connected:
                _connected.close()
                return True
                
    ## do a healthCheck 
    @retry(tries=3, delay=2, backoff=15) 
    def health_check(self,ip, port):
        print('dont forget')
        
