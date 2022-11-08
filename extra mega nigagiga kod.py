def kodicek(zdroj:str,kod:str)->str:
    nr=''
    p=0
    #zdroj=''
    kod_1= kod

    for i in range(len(zdroj)):
        while len(zdroj) != len(kod_1):
            kod_1= kod_1 + kod[p]
            p=p+1
            if p == (len(kod)-1):
                p=0
        a=ord(zdroj[i])
        k=ord(kod_1[i])
        a=(((a-97)+k)%26)+97
        b=chr(a)
        nr+=b
    return nr
print(kodicek('jejo dasda','kvet'))


