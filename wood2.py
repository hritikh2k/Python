wood1=int(input("enter length="))
wood2=int(input("enter length="))
a,b=0,0
main=(a+b)//4
if wood1<wood2:
    a=wood2
    b=wood1
else:
    a=wood1
    b=wood2
if b==0:
    
    print(c)
elif a//b<2:
    
    for i in range(main,0,-1):
        if a//i==b//i:
            print(i)
            break
elif a//b>=2:
    
    if b//main<1:
        main=main-(main-b)
        print(main)
    
    else:
        for i in range(main,0,-1):
            if a//i==3:
                print(i)
                break
                
            
