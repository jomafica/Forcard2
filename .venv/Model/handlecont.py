from handleconn import HandleConnection
from handlehref import HandleHref
from bs4 import BeautifulSoup
import json
import re

class Article():

    def __init__(self, body, set_id_href):
        self.body = body
        self.set_id_href = set_id_href
    








    def check_if_works(self):
        return self.body, self.set_id_href


domain='https://pplware.sapo.pt/linux/lakka-a-distro-que-transforma-o-seu-pc-numa-consola-retro/'

fetch_body=HandleConnection(domain).start() 
parse_body = HandleHref(fetch_body)

x = parse_body.get_article_id_href()
print(x)

#x = Article(body=parse_body.get_article_html_body(), set_id_href=parse_body.get_article_id_href())
#print(x.check_if_works())





