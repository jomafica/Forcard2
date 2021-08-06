from article_constructor import Article
from json_constructor import JsonConstructor
from reachable import ConnectionStatus
from bs4 import BeautifulSoup

def main():
    connection = ConnectionStatus()
    get_pages = Article()

    starter_domain = 'https://pplware.sapo.pt/'
    connection.start(starter_domain)

    while connection.STATUS:        
        pages = get_pages.get_total_pages()
        for page in range(pages[0], pages[1] + 1):
            domain = 'https://pplware.sapo.pt/page/' + str(page)
            print(domain)




if __name__ == "__main__":
    main()
