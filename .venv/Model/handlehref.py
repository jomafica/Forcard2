from bs4 import BeautifulSoup
import re    
    
class HandleHref: 

    def __init__(self, body):
        self.body = body

    def get_body_parsed(self, body):
        return BeautifulSoup(body, 'html.parser')
    
    # Return: {(ID_ARTICLE,HREF),(...)}
    def get_article_id_href(self):
        _set = set()
        for e in self.get_body_parsed(self.body).find_all("article"):
            rx = re.search(r'[^post-]+.', e['id'])
            _set.add((rx.group(0),e.a['href']))
        return _set

    def get_article_html_body(self, articleHtml):
        return [self.get_body_parsed(articleHtml).find_all("article")[0]]
    
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



        