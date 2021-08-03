
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
