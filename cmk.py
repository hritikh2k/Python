n=int(input('Enter number:'))
st=[]
a=0
q=0

for i in range(n):
    if i<2:
        st.append(i)
for j in range(n-1):
    p,t,r=0,0,0
    b,c,d,e,f,g=0,0,0,0,0,0
    if st[j]<10 and st[j+1]<10:
        a+=1
        q=st[j]+st[j+1]
        st.append(q)
    elif st[j]>10 and st[j+1]<10:
        a+=1
        p,t,r=0,0,0
        p=q%10
        t=q//10
        r=p+t
        q=r+st[j]
        st.append(q)
        
    elif st[j]>10 and st[j+1]>10:
        a+=1
        b,c,d,e,f,g=0,0,0,0,0,0
        b=q%10
        c=q//10
        d=b+c
        e=st[j-1]%10
        f=st[j-1]//10
        g=e+f
        q=d+g
        st.append(q)
    elif st[j]<10 and st[j+1]>=10:
        a+=1
        e,f,g=0,0,0
        e=st[j]%10
        f=st[j]//10
        g=e+f
        q=g+q
        st.append(q)
    
        
print(st,a+1,b,c,p,t)
