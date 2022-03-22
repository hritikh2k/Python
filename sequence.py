n=int(input('enter number:'))
r,w,h=0,1,0
st=[0]
for i in range(n):
    r+=w
    w=h
    h=r
    st.append(r)
    
    if r>9:
        f=0
        g=str(r)
        for j in g:
            p=int(j)
            f=f+p
        r=f
        h=r
print(st[n],st)    
        
    
  
