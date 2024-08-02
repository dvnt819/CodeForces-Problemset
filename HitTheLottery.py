x=int(input())
count=0
if x/100>=1:
    count = count + int(x / 100)
    x=x%100
if x/20>=1:
    count = count + int(x / 20)
    x=x%20
if x/10>=1:
    count = count + int(x / 10)
    x=x%10
if x/5>=1:
    count = count + int(x / 5)
    x=x%5
if x/1>=1:
    count = count + int(x / 1)
    x=x%1
print(count)
