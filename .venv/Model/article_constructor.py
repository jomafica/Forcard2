from bs4 import BeautifulSoup
import re
from typing import List, Set   

class Article(): 

    # Ver como guardar temporariamente o corpo do article sem ter que chamar sempre BS4. Var ou outra coisa?

    def __init__(self, body = None):
        self.body = body

    def get_body_parsed(self, body):
        return BeautifulSoup(body, 'html.parser')

    def get_total_pages(self, current_page : int = 1) -> List:
        '''
        return self.get_body_parsed(self.body).select('a[class="page-numbers"]')[1].string.replace('.','')

        '''
        return [current_page,int(self.get_body_parsed(self.body).select('a[class="page-numbers"]')[1].string.replace('.',''))]

    # Return: {(ID_ARTICLE,HREF),(...)} NOT ORDERED
    def get_article_id_href_home(self) -> Set:
        _set = set()
        for e in self.get_body_parsed(self.body).find_all("article"):
            rx = re.search(r'[^post-]+.', e['id'])
            _set.add((rx.group(0),e.a['href']))
        return _set

    def get_article_html_body(self) -> List:
        return self.get_body_parsed(self.body).find_all("article")[0]
    
    # Return: [<article>(...)</article>]
    def iter_article_set(self, article_set) -> List:
        for element in article_set:
            (_, _href) = element
            for link in _href:
                return self.get_article_html_body(link)

    # Return: {'786424', '786421', '786425'} # priorities passed need to be a set() type
    def compare_id(self, old_set, current_set) -> Set:
        return current_set.difference(old_set)
    
    #Try to find a meaning for this
    def is_not_last_id(self):
        pass






'''
    # Nao e necessario fazer isto! iterar SET acima criado e fazer parse de cada href
    def get_article_id_href(self):
        _set = set()
        _id = self.get_body_parsed(self.body).find_all("article")[0].find_all_next('span')[1]
        rx = re.search(r'[^more-]+.', _id['id'])
        #_set.add((rx.group(0),_y.a['href']))
        print(rx.group(0))
        return _set
'''

        