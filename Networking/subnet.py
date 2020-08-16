# python program for subnetting
# Enter ip address(any class), no. of hosts in each subnet and
# no. of subnets.
# returns all possible subnets.

ip=input('Enter ip address')
sNo=int(input('Enter no. of segments'))
hNo=int(input('Enter max no. of hosts in the subnet'))
a,b,c,d=ip.split('.')
a=int(a)
b=int(b)
c=int(c)
d=int(d)
tS=1
pS=0
while(tS<sNo):
    tS=tS*2     
    pS=pS+1    #no. of bits for subnet addr.
tH=1
pH=0
while(tH<hNo):
    tH=tH*2
    pH=pH+1   #no. of bits for hosts in each subnet.
check=0;
classF="";
if 1<=a<=127:
    print("This is class A ip")
    classF="A"
    if pS+pH > 24:
        check=check+1
    else:
        f='255.'
        if pS<=8:
            u=128
            sum=0
            while(pS>0):    
                sum=sum+u
                u=u/2
                pS=pS-1
            f=f+str(int(sum))+".0.0"
        elif pS<=16:
            pS=pS-8
            u=128
            sum=0
            while(pS>0):    
                sum=sum+u
                u=u/2
                pS=pS-1    
            f=f+"255."+str(sum)+".0"
        else: 
            pS=pS-16
            u=128
            sum=0
            while(pS>0):    
                sum=sum+u
                u=u/2
                pS=pS-1    
            f=f+"255.255."+str(sum)
        print("Subnet mask is ", f)    
elif 128<=a<=191:
    print("This is class B ip")
    classF="B"
    if pS+pH > 16:
        check=check+1
    else: 
        f='255.255.'
        if pS<=8:
            u=128
            sum=0
            while(pS>0):    
                sum=sum+u
                u=u/2
                pS=pS-1
            f=f+str(sum)+".0"
        else:
            pS=pS-8
            u=128
            sum=0
            while(pS>0):    
                sum=sum+u
                u=u/2
                pS=pS-1    
            f=f+"255."+str(sum)
        print("Subnet mask is ", f)        
elif 192<=a<=223:
    print("This is class C ip")
    classF="C"
    if pS+pH > 8:
        check=check+1
    else:
        f='255.255.255.'
        u=128
        sum=0
        while(pS>0):    
            sum=sum+u
            u=u/2
            pS=pS-1
        f=f+str(sum)
        print("Subnet mask is ", f)    
elif 224<=a<=239:    
    print("This is class D ip")
    check=check+1
elif 240<=a<=225:        
    print("This is class E ip")
    check=check+1

if check==1:
    print("Subnetting not possible")
else:
    print("Network id:         Range:                        Broadcast address:")
    if classF=="C":
        r=0
        while(r<256):
            f=str(a)+"."+str(b)+"."+str(c)+"."+str(r)+"     "+str(a)+"."+str(b)+"."+str(c)+"."+str(r+1)+" to "+str(a)+"."+str(b)+"."+str(c)+"."+str(r+tH-2)   
            f=f+"                "+str(a)+"."+str(b)+"."+str(c)+"."+str(r+tH-1)
            r=r+tH
            print(f)
    elif classF=="B":
        sums=0
        r=0
        q=0
        while(q<256):
            f=str(a)+"."+str(b)+"."+str(q)+"."+str(r)
            f=f+"     "+str(a)+"."+str(b)+"."+str(q)+"."+str(r+1)+" to "
            sums=sums+tH
            q=int(sums/256)
            r=int(sums%256)
            if r==0:
                h=q-1
                i=256-2
            else:
                h=q
                i=r
            f=f+str(a)+"."+str(b)+"."+str(h)+"."+str(i)   
            f=f+"                "+str(a)+"."+str(b)+"."+str(h)+"."+str(i+1)
            print(f)            
    elif classF=="A":
        sums=0
        r=0
        q=0
        q2=0
        while(q2<256):
            f=str(a)+"."+str(q2)+"."+str(q)+"."+str(r)
            f=f+"     "+str(a)+"."+str(q2)+"."+str(q)+"."+str(r+1)+" to "
            sums=sums+tH
            q=int(sums/256)
            if q>=256:
                q2=int(q/256)
                q=int(q%256)
            r=int(sums%256)
            if r==0:
                if q==0:
                    u=int(q2-1) 
                    h=int(256-1)
                else:   
                    h=int(q-1)
                i=int(256-2)
            else:
                h=int(q)
                i=int(r)
                u=int(q2)
            f=f+str(a)+"."+str(u)+"."+str(h)+"."+str(i)   
            f=f+"                "+str(a)+"."+str(u)+"."+str(h)+"."+str(i+1)
            print(f)            













