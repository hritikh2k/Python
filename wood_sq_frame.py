wood1=int(input("enter length="))
wood2=int(input("enter length="))
a,b=0,0
if wood1<wood2:
    a=wood2
    b=wood1
else:
    a=wood1
    b=wood2
if b==0:
    c=a//4
    print(c)
elif a//b<2:
    d=a+b
    e=d//4
    for i in range(e,0,-1):
        if a//i==b//i:
            print(i)
            break
elif a//b>=2:
    f=a+b
    g=f//4
    if b//g<1:
        g=g-(g-b)
        print(g)
    
    else:
        for i in range(g,0,-1):
            if a//i==3:
                print(i)
            break
                
            
