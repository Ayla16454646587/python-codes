def palind(r):
    e=len(r)-1
    s=0
    while(s<0):
        if (r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True
    
r=(1,2,3,3,2,1)

if(palind(r)):
    print("the Tuple is flipflop")
else:
    print("the tuple is not flip-flop")