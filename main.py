import sys
stdoutOrigin=sys.stdout
sys.stdout=open('output.txt','w')
#Check the words having special Characters.
def check_special(a):
    sp='!@#$%^&*()_-+=,.<>/?;:"\''
    if any(c in sp for c in a):
        return True
    return False

f=open('text.txt','r')
c=0
sp='!@#$%^&*()_-+=,.<>/?;:"\''
spc=0
a={}
for i in f:
    for j in i.split():
        if check_special(j):
            k=0
            while check_special(j):
                if j[k] in sp:
                    j=j[:k]+j[k+1:]
                    k-=1
                    spc+=1
                else:
                    k+=1
        try:
                a[len(j)]+=1
        except:
                a[len(j)]=1
        c+=1
a=sorted(a.items())
for i in a:
    print('There are ',i[1],'words with length',i[0])
print('There are ',spc,'Special Characters in file')
print('There are',c,'Total words in the file')
sys.stdout.close()
sys.stdout=stdoutOrigin