def shifrovka (word, key):
        result = ''
        r=[]
        t=[]
        for l,k in zip(word,key):
                r+=l
                t+=k
        for i in range((len(r))):
                b=int(t[i])
                result+= str(r[b])
        return result
                
def deshifrovka (word, key):
        result = ''
        r=[]
        t=[]
        for l,k in zip(word,key):
                r+=l
                t+=k
        for i in range((len(r))):
                a=str(i)
                b=int(t.index(a))
                result+= str(r[b])
        return result              
w = open('Source.txt')
for line in w:
    word=line
k1 = open('Key.txt')
for line in k1:
    key=line
b = open('Coded.txt','w')
a = open('DeCoded.txt','w')
c=(shifrovka (word, key))
d=(deshifrovka (word,key))
for index in c:
        b.write(index)
b.close()
for index in d:
        a.write(index)
a.close()
