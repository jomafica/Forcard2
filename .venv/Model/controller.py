from article_constructor import Article
from json_constructor import JsonConstructor
from connection_reliability import Connection
from bs4 import BeautifulSoup

def main():
    starter_domain = 'https://pplware.sapo.pt/'
    get_pages = Article(Connection(starter_domain).start())
    pages = get_pages.get_total_pages()
    for page in range(pages[0], pages[1] + 1):
        domain = 'https://pplware.sapo.pt/page/' + str(page)
        print(domain)
    #while connection_reliabilty.Connection(domain):
    #    page +=1 


if __name__ == "__main__":
    main()
