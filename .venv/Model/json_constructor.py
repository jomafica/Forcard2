from article_constructor import Article
from dataclasses import dataclass, field
import re

@dataclass(init=True)
class JsonConstructor(Article):

    tuple_article: tuple
    _id: int = None
    _href: str = None
    _body: str = None
    jsonbody: dict = field(default_factory=dict)

    #def __init__(self, tuple_article):
    #    self.tuple_article = tuple_article
    #    self._id = None
    #    self._href = None
    #    self._body = None
    #    self.jsonbody = {}

    def json_constructor(self, id, 
            href, body):
        self._append_id_and_href(id, href)
        self.get_time(body)
        self.get_comments(body)
        self.get_type(body)
        self.get_author(body)
        self.get_title(body)
        self.get_image(body)
        self.get_content(body)
    
    def check_tuple(self):
        if self.tuple_article:
            (id, href, body) = self.tuple_article
            if id and href and body != '' and id and href and body != None:
                self._id = id
                self._href = href
                self._body = body
                return True

    def get_json_body(self):
        try:
            if self.check_tuple():
                self.json_constructor(
                        self._id,self._href,
                        self._body)
                return self.jsonbody
        except:
            print('Html body is empty')
            pass
    
    def _append_id_and_href(self, id, href):
        self.jsonbody['id'] = id
        self.jsonbody['href'] = href

    def get_time(self, body):
        self.jsonbody['time'] = body.find('time').string

    def get_comments(self, body):
        rx = re.search(r'\d', body.find_all_next('a')[1].string)
        self.jsonbody['comments'] = rx.group(0)

    def get_type(self, body):
        self.jsonbody['type'] = body.a.string

    def get_author(self, body):
        self.jsonbody['author'] = body.select_one('a[rel="author"]').string

    def get_title(self, body):
        self.jsonbody['title'] = body.find('h1').string
    
    def get_image(self, body):
        self.jsonbody['image'] = body.find('img')['src']
    
    def get_content(self, body):
        x = body.select('p')
        temp_string = ''
        for y in x:
            if y.string:
                rgx = re.search(r'[\<].*[\>]', y.string)
                if not rgx:
                    temp_string += y.string.strip()
        self.jsonbody['content'] = temp_string

    # for test porpose
    def check_if_works(self):
        return self.body, self.set_id_href




'''

Following is used to test the above class

'''
#from reachable import ConnectionStatus
#domain_1='https://pplware.sapo.pt/'
#domain='https://pplware.sapo.pt/redes_sociais/#twitter-estabelece-parceria-com-a-reuters-e-a-ap-para-detetar-desinformacao/'
#
#fetch_body = ConnectionStatus().start(domain) 
#parse_body = Article(domain)
#
##fetch_body1 = HandleConnection(domain1).start() 
##parse_body1 = HandleHref(fetch_body1).get_article_id_href_home()
##print(parse_body1)
#
#y = Article(('786420', domain, parse_body.get_article_html_body())) # need to #pass a TUPLE
#print(y.get_json_body())









