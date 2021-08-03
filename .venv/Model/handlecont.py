from handleconn import HandleConnection
from handlehref import HandleHref
from bs4 import BeautifulSoup
import json
import re

class Article():

    def __init__(self, body=None):
        self.body = body
    
    def retunr_content(self):
        return self.body


domain='https://pplware.sapo.pt/linux/lakka-a-distro-que-transforma-o-seu-pc-numa-consola-retro/'
fetch_body=HandleConnection(domain).start()
parsed = HandleHref(fetch_body)
parsedD= parsed.get_article_html_body(fetch_body)

print(parsedD)
x = Article(body=parsedD)
#print(x.retunr_content())


