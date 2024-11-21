def yu(n,text):
    small = 'abcdefghijklmnopqrstuvwxyz'
    big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    leng=len(text)
    c = ""
    print(leng,text)
    for i in range(leng):
        size=text[i]
        print(size)
        size_=0
        size_=ord(size)
        if size_>=97 and size_<=122:
            jum= 26 - small.index(text[i])
            print(small[i])
            if n>jum:
                jump=n%26
                y=i+jump
            else:
                y=i+n
            simvol=small[y]
        c=c+simvol
    print(c)
                
        
        
def vaild():
    try:
        n=int(input())
        text=input()
    except:
        print("error")
    yu(n,text)
vaild()
