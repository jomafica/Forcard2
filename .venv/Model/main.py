from article_constructor import Article
from json_constructor import JsonConstructor
from reachable import StartConnection
from bs4 import BeautifulSoup
from time import sleep

def main():
    connection = StartConnection()
    starter_domain = 'https://pplware.sapo.pt/'
    connection.start(starter_domain)

    #get_pages = Article()
    #Nao estou a fazer fetch do codigo html em lado nenhum... 

    while connection._status:
        print('lol')
        connection.health_check()
        sleep(5)
        #pages = get_pages.get_total_pages()
        #for page in range(pages[0], pages[1] + 1):
        #    domain = 'https://pplware.sapo.pt/page/' + str(page)
        #    print(domain)

if __name__ == "__main__":
    main()
