
    # Test (apagar)
    #oldSet = {'786420', '786353', '786347', '786301', '786335'}
    #currentSet = {'786425', '786424', '786422', '786421', '786420', '786353', '786347', '786301', '786335'}
    #z = currentSet.difference(oldSet)
    #print(z)
    ################################################
    #yz = BeautifulSoup(fetch_body, 'html.parser')
    #y = [yz.find_all("article")[0]]
    #print(y)
    ################################################
    # Test (apagar)
    #yz = BeautifulSoup(fetch_body, 'html.parser')
    #y = set()
    #for e in yz.find_all("article"):
    #    rx = re.search(r'[^post-]+.', e['id'])
    #    y.add((rx.group(0),e.a['href']))
    #for ih in y:
    #    (id, href) = ih
    #    print(id)


if __name__ == "__main__":
    main()



'''
Get post ID, not finished!
Result: set{'786420', '786353', '786347', '786301', '786335'}
'''
#with open('resul.html', 'w', encoding="utf-8") as f:
#    x = []
#    y = set()
#    for e in html_body.find_all("article"):
#        x.append(e)
#        y.add(e.a['href'])
#    print(y)
#    f.write(str(x))
#f.close()
##y = set()
##for e in html_body.find_all("article"):
##  rx = re.search(r'[^post-]+.', e['id'])
##  y.add(rx.group(0))      
## print(y)






'''
Requirements:
C    <h1 class="post-title">Lakka: A distro que transforma o seu PC numa consola retro</h1> 
C    <time datetime="2021-08-02T23:00:40+01:00">02 Ago 2021</time>
C    <a href="https://pplware.sapo.pt/category/linux/" title="Ver todos os artigos de Linux">Linux</a><span class="comments-link"><a href="https://pplware.sapo.pt/linux/lakka-a-distro-que-transforma-o-seu-pc-numa-consola-retro/#comments">1 Comentário</a></span>   
    <p>Pela internet existem projetos fantásticos... e gratuitos. O que damos a conhecer hoje chama-se Lakka, e é uma distribuição Linux que transforma facilmente o&nbsp;seu PC numa consola retrogaming.</p>
    <p>Conheça melhor esta distribuição que é baseada na LibreELEC.</p>
C   <p><a target="_blank" href="https://pplware.sapo.pt/wp-content/uploads/2021/08/lakka-retrogaming-linux.jpe"><img loading="lazy" src="https://pplware.sapo.pt/wp-content/uploads/2021/08/lakka-retrogaming-linux-720x405.jpe" alt="" width="720" height="405" class="aligncenter size-medium wp-image-787617" srcset="https://pplware.sapo.pt/wp-content/uploads/2021/08/lakka-retrogaming-linux-720x405.jpe 720w, https://pplware.sapo.pt/wp-content/uploads/2021/08/lakka-retrogaming-linux-150x84.jpe 150w, https://pplware.sapo.pt/wp-content/uploads/2021/08/lakka-retrogaming-linux-768x432.jpe 768w, https://pplware.sapo.pt/wp-content/uploads/2021/08/lakka-retrogaming-linux-345x194.jpe 345w, https://pplware.sapo.pt/wp-content/uploads/2021/08/lakka-retrogaming-linux-50x28.jpe 50w, https://pplware.sapo.pt/wp-content/uploads/2021/08/lakka-retrogaming-linux.jpe 800w" sizes="(max-width: 720px) 100vw, 720px"></a></p>
    <h3>Distribuição Linux Lakka tem suporte para Raspberry Pi</h3>
    <p>A distribuição Linux Lakka é um sistema "amigável" uma vez que é fácil de configurar e usar. Além disso, esta distribuição é também, “poderosa” graças ao facto de usar o RetroArch, o conhecido frontend multiplataforma para emuladores, videojogos, etc.</p>
    <p>Esta distribuição suporta vários tipos de hardware como o Raspberry Pi e outros mini-PCs semelhantes. A distribuição Linux Lakka é um projeto Open Source desenvolvido pela comunidade sendo baseado na popular distribuição Linux LibreELEC, uma distribuição destinada a sistemas multimédia.</p>
    <p>A distro Lakka é capaz de transformar um computador numa consola de jogos retro, com recurso a emuladores. Além da imagem x86 tradicional,&nbsp; suporta Raspberry Pi 0/W, Raspberry Pi, Raspberry Pi 2, Raspberry Pi 3, Raspberry Pi 4, I.MX6 Cubox-I, I.MX6 UDOO, I.MX6 Wandboard, Odroid XU3 /4, Allwinner, Amlogic, Rockchip, Odroid Go Advance, Ambernic RG351P / M, Ambernic RG351V e Nintendo Switch.</p>
    <p>Ao nível das consolas ou plataformas de videojogos, é capaz de emular a antiga Nintendo NES, Super Nintendo, Mega Drive (Sega Genesis no mercado norte-americano), PlayStation, jogos Arcade e muito mais graças ao RetroArch.</p>
    <p>Num próximo artigo iremos ensinar como podem usar esta distribuição. Estejam atentos.</p>
C   <h3><a href="https://pplware.sapo.pt/author/ppinto/" title="Artigos de Pedro Pinto" rel="author">Pedro Pinto</a></h3>




    JSONBODY:
    {
    "id": "POST_ID"
    "article": "ARTICLE_URL"
    "time": "DATE_TIME"
    "comments": "COMMENTS"
    "type":"CONTENT_TYPE"
    "author":"AUTHOR"
    "title": "ARTICLE_TITLE"
    "image": "URL_IMAGE"   
    "content":"ARTICLE_DOC"
    }
'''









