from handleconn import HandleConnection
from handlehref import HandleHref
from bs4 import BeautifulSoup
import json
import re

class Article(HandleHref):

    def __init__(self, body, set_id_href=None):
        self.body = body
        self.set_id_href = set_id_href
        self.jsonbody = {}

    def json_constructor(self):
        self._appen_id_and_href()
        self.get_time()
        self.get_comments()
        self.get_type()
        self.get_author()
        self.get_title()
        self.get_image()
        self.get_content()

    def get_json_body(self):
        self.json_constructor()
        return self.jsonbody
    
    def _appen_id_and_href(self):
        (_id, _href) = self.set_id_href
        self.jsonbody['id'] = _id
        self.jsonbody['href'] = _href

    def get_time(self):
        self.jsonbody['time'] = self.body.find('time').string

    def get_comments(self):
        rx = re.search(r'\d', self.body.find_all_next('a')[1].string)
        self.jsonbody['comments'] = rx.group(0)

    def get_type(self):
        self.jsonbody['type'] = self.body.a.string

    def get_author(self):
        self.jsonbody['author'] = self.body.select_one('a[rel="author"]').string

    def get_title(self):
        self.jsonbody['title'] = self.body.find('h1').string
    
    def get_image(self):
        self.jsonbody['image'] = self.body.find('img')['src']
    
    def get_content(self):
        x = self.body.select('p')
        temp_string = ''
        for y in x:
            if y.string:
                rgx = re.search(r'[\<].*[\>]', y.string)
                if not rgx:
                    temp_string += y.string.strip()
        self.jsonbody['content'] = temp_string

    def check_if_works(self):
        return self.body, self.set_id_href


#domain='https://pplware.sapo.pt/linux/lakka-a-distro-que-transforma-o-seu-pc-numa-consola-retro/'
domain='https://pplware.sapo.pt/redes_sociais/twitter-estabelece-parceria-com-a-reuters-e-a-ap-para-detetar-desinformacao/'

fetch_body=HandleConnection(domain).start() 
parse_body = HandleHref(fetch_body)

y = Article(parse_body.get_article_html_body(), set_id_href={'786420', domain})
print(y.get_json_body())










