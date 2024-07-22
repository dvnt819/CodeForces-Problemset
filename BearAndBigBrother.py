s=input()
l=s.split()
l1=int(l[0])
l2=int(l[1])
count=0
while(l1<=l2):
    l1=l1*3
    l2=l2*2
    count+=1
    
print(count)
