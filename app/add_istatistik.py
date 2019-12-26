def add_istatistik(lineList):
    for idx, item in enumerate(lineList):
        a = item.split('/')
        a.insert(5,"istatistik")
        link_updated =""
        print(a)
        for i in range(7):
            if i < 6:
                link_updated = link_updated + a[i] + "/"
            else:
                a[i] = a[i].replace('\n','')
                link_updated = link_updated + a[i] 
            print(link_updated)
        
        lineList[idx] = link_updated + "\n"

    with open('maclar.txt', 'w') as f:
        for item in lineList:
            f.write("%s" % item)
    
    return lineList
