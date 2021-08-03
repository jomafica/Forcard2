from bs4 import BeautifulSoup
import re    
    
class HandleHref: 

    # Ver como guardar temporariamente o corpo do article sem ter que chamar sempre BS4. Var ou outra coisa?

    def __init__(self, body):
        self.body = body

    def get_body_parsed(self):
        return BeautifulSoup(self.body, 'html.parser')
    
    # Return: {(ID_ARTICLE,HREF),(...)}
    def get_article_id_href_home(self):
        _set = set()
        for e in self.get_body_parsed().find_all("article"):
            rx = re.search(r'[^post-]+.', e['id'])
            _set.add((rx.group(0),e.a['href']))
        return _set

    # Nao e necessario fazer isto! iterar SET acima criado e fazer parse de cada href
    def get_article_id_href(self):
        _set = set()
        _id = self.get_body_parsed().find_all("article")[0].find_all_next('span')[1]
        rx = re.search(r'[^more-]+.', _id['id'])
        #_set.add((rx.group(0),_y.a['href']))
        print(rx.group(0))
        return _set

    def get_article_html_body(self):
        return [self.get_body_parsed().find_all("article")[0]]
    
    # Return: [<article>(...)</article>]
    def iter_article_set(self, articleSet):
        for element in articleSet:
            (_id, _href) = element
            for link in _href:
                return self.get_article_html_body(link)

    # Return: {'786424', '786421', '786425'}
    def compare_id(self, old_set, current_set):
        return current_set.difference(old_set)
    
    #Try to find a meaning for this
    def is_not_last_id(self):
        pass



        